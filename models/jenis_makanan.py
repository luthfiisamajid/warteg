from odoo import api, fields, models

class jenis_makanan(models.Model):
    _name = 'warteg.jenis'
    _description = 'New Description'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    person_in_charge = fields.Char(string='Person')
    posisi_rak = fields.Char(string='Posisi Rak')
    jenis_ids = fields.One2many(comodel_name='warteg.detail_makanan',
                                     inverse_name='detail_makanan_id',
                                     string='Detail Makanan')
    
    
    
    
    
