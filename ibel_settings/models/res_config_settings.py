from lxml import etree

from odoo import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def get_view(self, view_id=None, view_type='form', **options):
        ret_val = super().get_view(view_id=None, view_type='form', **options)

        doc = etree.XML(ret_val["arch"])

        query = "//setting[field[@widget='upgrade_boolean']]"
        for item in doc.xpath(query):
            item.attrib["class"] = "d-none"
        for block in doc.xpath("//block"):
            if (
                len(
                    block.xpath(
                        """setting[
                            not(contains(@class, 'd-none'))
                            and not(@invisible='1')]
                        """
                    )
                )
                == 0 and block.attrib["title"] != "About"
            ):
                # Removing title and tip so that no empty h2 or h3 are displayed
                block.attrib.pop("title", None)
                block.attrib.pop("tip", None)
                block.attrib["class"] = "d-none"

        ret_val["arch"] = etree.tostring(doc)
        return ret_val
