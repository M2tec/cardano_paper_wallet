# -*- coding: utf-8 -*-
from odoo import models, fields, api

from cardano.wallet import Wallet
from cardano.wallet import WalletService
from cardano.backends.walletrest import WalletREST

import subprocess

class POSConfig(models.Model):
    _inherit = 'pos.config'

    iface_orderline_pos_order_notes = fields.Boolean(string='Orderline Notes', help='Allow custom notes on Orderlines.')

    @api.onchange('module_pos_restaurant')
    def _onchange_module_pos_restaurant(self):
        if not self.module_pos_restaurant:
            self.update({'iface_printbill': False,
                         'iface_splitbill': False,
                         'is_order_printer': False,
                         'is_table_management': False,
                         'iface_orderline_notes': False,
                         'iface_orderline_pos_order_notes': True})

        else:
            self.update({'iface_orderline_pos_order_notes': False})
            
@api.model            
class POSOrderline(models.Model):
    _inherit = 'pos.order.line'
    
    def generate_cardano_wallet(self):
        print("generate_cardano_wallet")
        mnemonic = subprocess.run(["cardano-wallet", "recovery-phrase", "generate"])
        return mnemonic

   
        
