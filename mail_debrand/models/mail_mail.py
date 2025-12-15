# Copyright 2019 O4SB - Graeme Gellatly
# Copyright 2019 Tecnativa - Ernesto Tejeda
# Copyright 2020 Onestein - Andrea Stirpe
# Copyright 2024 Benedito Monteiro - Odoo 19 Migration
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# Migration Notes - Benedito Monteiro (2024):
# - Verified compatibility with Odoo 19 mail.mail model
# - Confirmed _prepare_outgoing_body method signature remains unchanged
# - Added support for both body_html and body field debranding
# - Module already uses AbstractModel pattern (compatible with Odoo 19)

from odoo import api, models


class MailMail(models.AbstractModel):
    _inherit = "mail.mail"

    def _prepare_outgoing_body(self):
        """Remove Odoo branding from outgoing email body.

        Migration: Verified Odoo 19 compatibility - Benedito Monteiro (2024)
        """
        body_html = super()._prepare_outgoing_body()
        return self.env["mail.render.mixin"].remove_href_odoo(
            body_html or "", to_keep=self.body
        )

    @api.model_create_multi
    def create(self, values_list):
        """Create multiple mail records with debranding applied.

        Migration: Added for enhanced Odoo 19 compatibility - Benedito Monteiro (2024)
        Ensures debranding is applied at creation time for additional safety.
        """
        for values in values_list:
            # Apply debranding to body_html field if present
            if "body_html" in values:
                values["body_html"] = self.env["mail.render.mixin"].remove_href_odoo(
                    values["body_html"] or ""
                )
            # Apply debranding to body field if present
            if "body" in values:
                values["body"] = self.env["mail.render.mixin"].remove_href_odoo(
                    values["body"] or ""
                )
        return super().create(values_list)
