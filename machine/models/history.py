from odoo import models, fields


class history(models.Model):
    _name = "machine.history"

    description = fields.Text()
    user_id = fields.Many2one('res.users', string="User")
    machine_ids = fields.Many2one('machine.machines', string="Machine")
