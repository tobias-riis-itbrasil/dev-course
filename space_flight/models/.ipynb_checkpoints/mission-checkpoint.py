# -*- Coding: utf-8 -*-

from odoo import models, fields, api

class mission(models.Model):
    _name = 'spaceflight.mission'
    _description = 'Space Flight Mission'
    
    space_ship_id = fields.Many2one(string='Selec Spaceship', comodel_name='spaceflight.spaceship')
    
    seats = fields.Char(relation='space_ship_id.seats')
    
    #crew_members = fields.Many2many