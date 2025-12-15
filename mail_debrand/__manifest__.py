# Copyright 2016 Tecnativa - Jairo Llopis
# Copyright 2017 Tecnativa - Pedro M. Baeza
# Copyright 2019 ForgeFlow S.L. - Lois Rilo <lois.rilo@forgeflow.com>
# 2020 NextERP Romania
# Copyright 2021 Tecnativa - João Marques
# Copyright 2024 Benedito Monteiro - Odoo 19 Migration
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# Migration to Odoo 19.0 - Benedito Monteiro (2024)
# This migration includes:
# - Update to support new QWeb template engine replacing Jinja
# - Adaptation to @api.model_create_multi decorator pattern
# - Support for inline template syntax {{}} instead of ${}
# - Compatibility with new mail.render.mixin methods
# Migration based on comprehensive research of Odoo 19 mail system changes

{
    "name": "Mail Debrand",
    "summary": """Remove Odoo branding in sent emails
    Removes anchor <a href odoo.com togheder with it's parent
    ( for powerd by) form all the templates
    removes any 'odoo' that are in tempalte texts > 20characters
    """,
    "version": "19.0.1.0.0",
    "category": "Discuss",
    "website": "https://github.com/OCA/social",
    "author": """Tecnativa, ForgeFlow, Onestein, Sodexis, Nexterp Romania,
             Odoo Community Association (OCA)""",
    "contributors": [
        "Jairo Llopis",
        "Pedro M. Baeza",
        "Lois Rilo",
        "João Marques",
        "Benedito Monteiro",  # Odoo 19 migration
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail"],
    "development_status": "Production/Stable",
    "maintainers": ["pedrobaeza", "joao-p-marques"],
}
