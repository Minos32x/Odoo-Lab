from odoo import models, fields


class tag(models.Model):
    _name = "machine.tags"

    name = fields.Char()
