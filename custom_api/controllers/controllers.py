from odoo import http
from odoo.http import request, Response
import json

class CustomApiController(http.Controller):

    @http.route('/custom_api/contacts', type='http', auth='private', methods=['GET'], csrf=False)
    def get_contacts(self, **kw):
        contacts = request.env['custom.api'].search([])
        contact_data = []
        for contact in contacts:
            contact_data.append({
                'name': contact.name,
                'email': contact.email,
            })

        response = {
            'status': 'success',
            'data': contact_data,
        }
        return Response(json.dumps(response), content_type='application/json;charset=utf-8')
