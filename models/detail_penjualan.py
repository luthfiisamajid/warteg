from odoo import api, fields, models

class detail_penjualan(models.Model):
    _name = 'warteg.detail_penjualan'
    _description = 'New Description'

    name = fields.Char(string='Name')
    
    jumlah_beli = fields.Integer(string='Jumlah Beli')
    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='jumlah_harga')
    detailmakanan_id = fields.Many2one(comodel_name='warteg.detail_makanan', string='Detail Makanan')
    hargamakanan = fields.Integer(compute='_compute_hargamakanan', string='hargamakanan')
    
    @api.depends('detailmakanan_id')
    def _compute_hargamakanan(self):
        for record in self :
            record.hargamakanan = record.detailmakanan_id.harga
    
    @api.depends('jumlah_beli','hargamakanan')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga=record.jumlah_beli*record.hargamakanan
    
    detpenjualan_ids = fields.Many2one(comodel_name='warteg.penjualan', string='Penjualan')
    
    
    
    
