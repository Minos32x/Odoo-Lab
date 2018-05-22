from odoo import models, fields,api


class machine(models.Model):
    _name = "machine.machines"

    name = fields.Char()
    description = fields.Text()
    price = fields.Integer()
    image = fields.Binary()
    department_id = fields.Many2one('department.departments', string="department")
    tag_id = fields.Many2many('machine.tags', string="Tags")
    history_id = fields.One2many('machine.history', 'machine_ids', string="History")
    state = fields.Boolean()
    approved_by=fields.Many2one('res.users','Approved By',default=lambda self: self.env.uid)
