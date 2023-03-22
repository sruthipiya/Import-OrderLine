from odoo import models


class ImportOrderLine(models.Model):
    _inherit = 'sale.order'

    def action_import_lines(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'upload.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }




