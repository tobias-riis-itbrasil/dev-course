# -*- Coding: utf-8 -*-

{
    
    'name': 'Space_flight',
    
    'version': '0.1',
    
    'author': 'Tobias Riis',
    
    'description': 'manages the tasks logistics to perfom a spaceflight, includes spaceship and space crew',
    
    'category': 'Utilities',
    
    'depends': ['base'],
    
    'data': [
        "views/spaceship.xml",
        'views/menuitems.xml',
        'security/space_flight_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'application': True,
    
    'demo': [
        'demo/spaceflight_demo.xml',
        
    ],
    
}