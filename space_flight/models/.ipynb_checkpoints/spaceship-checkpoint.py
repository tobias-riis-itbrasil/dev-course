# -*- Coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):
    _name = 'spaceflight.spaceship'
    _description = 'Space Flight Spaceship'
    
    
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
    
    main_tank_fuel = fields.Float(string="Main Tank Fuel, gallons", default=0.00)
    
    secondary_tank_fuel = fields.Float(string="Main Tank Fuel, gallons", default=0.00)
    
    total_fuel = fields.Float(string="Total Fuel", readonly=True)
    
    #relational fields of day 6
    
    mission_ids = fields.One2many(comodel_name='spaceflight.mission',
                                  inverse_name='space_ship_id',
                                  string='Missions')
    
    
    
    @api.onchange('main_tank_fuel', 'secondary_tank_fuel')
    def _onchange_fuel_price(self):
        
        if self.main_tank_fuel < 0.00:
            raise UserError['Fuel Amount cannot be negative']
        
        if self.secondary_tank_fuel < 0.00:
            raise UserError['Fuel Amount cannot be negative']
        
        self.total_fuel = self.main_tank_fuel + self.secondary_tank_fuel
    
    
    
    @api.constrains('crew_members')
    def _check_crew(self):
        for record in self:
            if record.crew_members < 2:
                raise ValidationError('Always bring at least two crew members: %s' %record.crew_members)
    
    #later: crew = fields.Many2many()
    
    
    