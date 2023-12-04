{
    'name': "My Animated Snippets",
    'version': '16.0.1.0.0',
    'summary': """Animated Snippets for Websites.""",
    'description': """Variety of Snippets With Animations to Beautify your Website.""",
    'author': "",
    'company': '',
    'maintainer': '',
    'category': 'Website',
    'website': "",
    'depends': ['base', 'website', 'web_editor'],
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/animated_square_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/animated_snippet/static/src/css/animated_square.css',

        ]},
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
