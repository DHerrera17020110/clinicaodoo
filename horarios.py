# -*- coding: utf-8 -*-
from odoo import models, fields

class horarios(models.Model):
    _name = "clinica.horarios"

    name=fields.Char(string='Horario')
    doctor = fields.Many2one('clinica.doctores', require='True', string='Doctor')
    id_horario = fields.Char(string='Clave Horario')
    numconsult = fields.Char(string='# Consultorio')
  #  periodo = fields.Many2one('escolares.periodos', requireT='True', string='Periodo')
  #  plan = fields.Many2one('escolares.planes', require='True', string='Plan de estudio')
  #  nivel = fields.Many2one('escolares.niveles', require='True', string='Niveles')
    
    _sql_constraints = [
        ('unique_horarios', 'unique (name)', 'El horario ya existe!')
    ]

