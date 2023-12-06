from odoo import models, fields, api

class CustomApi(models.Model):
    _name = 'custom.api'
    _description = 'Custom API'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
