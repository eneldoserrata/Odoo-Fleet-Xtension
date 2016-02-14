# -*- coding: utf-8 -*-
{
    'name': "Fleet Xtenson - Vehicle Gallery",
    'summary': "Gallery that shows damages overtime",
    'author': "Salton Massally <smassally@idtlabs.sl>",
    'website': "http://idtlabs.sl",
    'category': 'Managing vehicles and contracts',
    'version': '0.1',
    'depends': ['fleet_x'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_gallery.xml',
        'views/inspection_report.xml'
    ],

    'installable': True

}
