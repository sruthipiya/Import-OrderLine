{
    'name': 'Import Order Lines',
    'description': 'Import order lines',
    'version': '16.0.1.0.0',
    'summary': 'Import order lines into sale',
    'installable': True,
    'application': True,
    'sequence': 1,

    'depends': ['base', 'sale'],
    'data': ['security/ir.model.access.csv', 'views/import_line.xml', 'views/upload_wizard.xml']
}
