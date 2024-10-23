from odoo import models, fields


class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Real Estate Property Type"
    _sql_constrains = [("unique_name", "UNIQUE(name)", "Type name has to be unique")]

    name = fields.Char(string="Name", required=True)
