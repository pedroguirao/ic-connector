from odoo import api, fields, models 
from odoo.exceptions import ValidationError

import logging
from requests.auth import HTTPBasicAuth
from requests import Session
from odoo.osv import osv
import xmlrpc.client


class ConectorPartners(models.Model):
    _inherit = 'res.partner'
        
    id_remoto = fields.Integer(
        string='Identificador remoto',
    )
    is_sync = fields.Boolean(
        string='Sincronizar',
    )

    #@api.constrains('is_sync')
    #def _partner_sync(self):
    #    for partner in self:
    #        self.x_name = self.x_di_id.x_codigo_di
    #    if self.x_di_id.x_estado != False:
    #        self.x_estado = self.x_di_id.x_estado        

    @api.multi
    def partner_sync_button(self):
        
        dbodoo = "gp_pruebas"
        userodoo = "serin"
        passodoo = "ic2015$$"
        urlodoo = "51.91.158.27"

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(urlodoo))
        uid = common.authenticate(dbodoo, userodoo, passodoo, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(urlodoo))

        for partner in self:
            partner.id_remoto = models.execute_kw(dbodoo, uid, passodoo, 'res.partner', 'create', [{
                'name':partner.name,
                #'parent_id':partner.parent_id,
                #'type':partner.type,
                'vat':partner.vat,
                #'street':partner.street,
                #'city':partner.city,
                #'state_id':partner.state_id,
                #'zip':partner.zip,
                #'country_id':partner.country_id,
                #'function':partner.function,
                #'phone':partner.phone,
                #'mobile':partner.mobile,
                'email':partner.email,
                #'website':partner.website,
                #'title':partner.title,
                #'lang':partner.lang,
                #'customer':partner.customer,
                #'user_id':partner.user_id,
                #'opt_out':partner.opt_out,
                #'message_bounce':partner.message_bounce,
                #'supplier':partner.supplier,
                #'ref':partner.ref,
                #'company_id':partner.company_id, 
              
                        
                
            }])



        
        
        



