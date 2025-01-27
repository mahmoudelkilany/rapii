# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
import json
import werkzeug.wrappers






class ApiRapii(http.Controller):

    @http.route('/api/crm', methods=['POST'], type="http", auth='public', csrf=False)
    def post_crm(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env["crm.lead"].sudo().create(vals)
        if res:
            return[{
                "message": "Lead  has been created"
            }]



    @http.route('/api/products', methods=['GET'], type="json", auth='public', csrf=False)
    def get_products(self):
        try:
            product_ids = request.env["product.product"].sudo().search([])
            if not product_ids:
               return [{
                 "message": "Product Not Exist",
               }]
            return [{
               "id": product_id.id,
               "name": product_id.name,
               "attribute": product_id.product_template_variant_value_ids,
                "categories" : product_id.categ_id

            } for product_id in product_ids]
        except Exception as error:
            return [{
                "error": error,
            }]








