from odoo import api, fields, models 
from odoo.exceptions import ValidationError

import logging
from odoo.osv import osv



class ResCompany(models.Model):
    _inherit = 'res.company'
        
    dbodoo = fields.Char(
        string='DB',
    )
    userodoo = fields.Char(
        string='Usr',
    )
    passodoo = fields.Char(
        string='Passwd',
    )
    urlodoo = fields.Char(
        string='Url',
    )



        
        
        



