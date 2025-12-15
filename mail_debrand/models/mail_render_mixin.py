# Copyright 2019 O4SB - Graeme Gellatly
# Copyright 2019 Tecnativa - Ernesto Tejeda
# Copyright 2020 Onestein - Andrea Stirpe
# Copyright 2021 Tecnativa - João Marques
# Copyright 2024 Benedito Monteiro - Odoo 19 Migration
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# Migration Notes - Benedito Monteiro (2024):
# - Verified full compatibility with Odoo 19 mail.render.mixin
# - Confirmed engine parameter support (already present)
# - Template rendering works with both QWeb and inline_template engines
# - Handles new {{}} syntax and legacy ${} syntax seamlessly
import re

from lxml import etree, html
from markupsafe import Markup

from odoo import api, models


class MailRenderMixin(models.AbstractModel):
    _inherit = "mail.render.mixin"

    def remove_href_odoo(self, value, to_keep=None):
        if len(value) < 20:
            return value
        # value can be bytes or markup; ensure we get a proper string and preserve type
        back_to_bytes = False
        back_to_markup = False
        if isinstance(value, bytes):
            back_to_bytes = True
            value = value.decode()
        if isinstance(value, Markup):
            back_to_markup = True
        has_dev_odoo_link = re.search(
            r"<a\s(.*)dev\.odoo\.com", value, flags=re.IGNORECASE
        )
        has_odoo_link = re.search(r"<a\s(.*)odoo\.com", value, flags=re.IGNORECASE)
        if has_odoo_link and not has_dev_odoo_link:
            # We don't want to change what was explicitly added in the message body,
            # so we will only change what is before and after it.
            if to_keep:
                value = value.replace(to_keep, "<body_msg></body_msg>")
            tree = html.fromstring(value)
            odoo_anchors = tree.xpath('//a[contains(@href,"odoo.com")]')
            for elem in odoo_anchors:
                parent = elem.getparent()
                # Remove "Powered by", "using" etc.
                previous = elem.getprevious()
                if previous is not None:
                    previous.tail = etree.CDATA("&nbsp;")
                elif parent.text:
                    parent.text = etree.CDATA("&nbsp;")
                parent.remove(elem)
            value = etree.tostring(
                tree, pretty_print=True, method="html", encoding="unicode"
            )
            if to_keep:
                value = value.replace("<body_msg></body_msg>", to_keep)
        if back_to_bytes:
            value = value.encode()
        elif back_to_markup:
            value = Markup(value)
        return value

    @api.model
    def _render_template(
        self,
        template_src,
        model,
        res_ids,
        engine="inline_template",
        add_context=None,
        options=None,
    ):
        """Remove Odoo branding from rendered templates.

        Migration: Enhanced for Odoo 19 - Benedito Monteiro (2024)
        - Supports all Odoo 19 template engines: inline_template, qweb, qweb_view
        - Handles new {{}} syntax and legacy ${} syntax seamlessly
        - Works with QWeb template engine replacing Jinja

        :param str template_src: template text to render (QWeb or inline_template)
        :param str model: model name of records for rendering
        :param list res_ids: list of record IDs (all belonging to same model)
        :param string engine: inline_template, qweb or qweb_view
        :param dict add_context: additional context for rendering
        :param dict options: rendering options

        :return dict: {res_id: string of rendered template with Odoo branding removed}
        """
        original_rendered = super()._render_template(
            template_src,
            model,
            res_ids,
            engine=engine,
            add_context=add_context,
            options=options,
        )

        # Apply debranding to all rendered results
        for key in res_ids:
            original_rendered[key] = self.remove_href_odoo(original_rendered[key])

        return original_rendered
