import openpyxl, base64
from io import BytesIO
from odoo import models, fields


class UploadWizard(models.TransientModel):
    _name = 'upload.wizard'

    upload_file = fields.Binary(string='Upload file')

    def action_import(self):
        print("bin", self.upload_file)
        order = openpyxl.load_workbook(
            filename=BytesIO(base64.b64decode(self.upload_file)))
        xl_order = order.active
        print('xl_order', order)
        for record in xl_order.iter_rows(min_row=2, max_row=None, min_col=None,
                                         max_col=None, values_only=True):
            product = self.env['product.product'].search(
                [('name', '=', record[0])], limit=1)
            if not product:
                # print("inside if")
                product = self.env['product.product'].create({
                    'name': record[0]
                })
            uom = self.env['uom.uom'].search([('name', '=', record[2])])
            if not uom:
                uom = self.env['uom.uom'].browse([1])
            active_id = self.env['sale.order'].browse(
                self.env.context.get('active_id'))
            active_id.order_line = [(0, 0, {
                'product_id': product.id,
                'product_uom_qty': record[1],
                'product_uom': uom.id,
                'name': record[3],
                'price_unit': record[4],
                'order_id': active_id.id
            })]
