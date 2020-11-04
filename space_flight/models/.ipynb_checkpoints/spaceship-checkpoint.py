# -*- Coding: utf-8 -*-

from odoo import models, fields

class Spaceship(models.Model):
    _name = 'spaceflight.spaceship'
    
    
    name = fields.Char(string='Name of the Ship', required=True)
    
    description = fields.Text(string='Description of this vessel')
    
    seats = fields.Integer(string='How many seats?')
    
    serial_no = fields.Char()
    
    type = fields.Char('Which type of spaceship is this')
    
    fuel_type = fields.Selection(string='Choose Fuel',
                                 selection=[('nitrogen', 'Nitrogen'),
                                            ('coal', 'Coal'),
                                            ('hydrogen', 'Hydrogen')]
                                )
    
    
    active = fields.Boolean(string='Is this ship active?')
    
    
    #later: crew = fields.Many2many()
    
    
    