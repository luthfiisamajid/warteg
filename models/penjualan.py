from odoo import api, fields, models

class penjualan(models.Model):
    _name = 'warteg.penjualan'
    _description = 'New Description'

    name = fields.Char(string='Name')
    kode_penjualan = fields.Integer(string='Kode Penjualan')
    tanggal_penjualan = fields.Date(string='Tanggal Penjualan',default=fields.Date.today)
    dtlpnjln = fields.One2many(comodel_name='warteg.detail_penjualan',
                                     inverse_name='detpenjualan_ids',
                                     string='Detail Penjualan')
    total_harga = fields.Integer(compute='_compute_total_harga', string='total_harga')
    
    @api.model
    def _compute_total_harga(self):
        for record in self:
            total=sum(self.env['warteg.detail_penjualan'].search([('detpenjualan_ids','=',record.id)]).mapped('jumlah_harga'))
            record.total_harga=total
