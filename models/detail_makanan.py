from odoo import api, fields, models

class detail_makanan(models.Model):
    _name = 'warteg.detail_makanan'
    _description = 'New Description'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    stok = fields.Integer(string='Stok')
    harga = fields.Integer(string='Harga')
    detmakanan_ids = fields.One2many(comodel_name='warteg.detail_penjualan',
                                     inverse_name='detailmakanan_id',
                                     string='Detail Makanan')
    detail_makanan_id = fields.Many2one(comodel_name='warteg.jenis', string='Jenis Makanan')


    
    
    
