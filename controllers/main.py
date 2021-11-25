# coding: utf-8
import logging
import pprint
import json
import subprocess
from odoo import fields, http
from odoo.http import request

_logger = logging.getLogger(__name__)


class PosMnemonicController(http.Controller):
    @http.route('/pos_cardano/mnemonic', type='http', methods=['POST','GET'], auth='none', csrf=False)
    def mnemonic(self):
        _logger.info('-----mnemonic--------')
        
        mnemonic = subprocess.check_output(["cardano-wallet", "recovery-phrase", "generate"], universal_newlines=True)
                
        json_dict = {"mnemonic": mnemonic}
        #json_dict = { "name" : "jimmy", "age": "10"}
        print(json_dict)

        json_obj = json.dumps(json_dict)
               
        return json_obj

