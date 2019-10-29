{
    'name': "connector partners",

    'summary': """
        Modulo para sincornizar partners desde Green""",

    'description': """
        Modulo para sincornizar partners desde Green
    """,

    'author': "Pedro Baños Guirao",
    'website': "https://ingenieriacloud.com",

    'category': 'Tools',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
    ],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/connector_partner_view.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}