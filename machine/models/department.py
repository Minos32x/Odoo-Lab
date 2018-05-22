from odoo import models, fields


class department(models.Model):
    _name = "department.departments"

    name = fields.Char()
    machine_ids = fields.One2many('machine.machines','department_id')

