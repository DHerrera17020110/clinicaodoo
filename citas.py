# -*- coding: utf-8 -*-
from odoo import models,fields,api

class citas(models.Model):
    _name = 'clinica.citas'

    ide = fields.Char(string='CLAVE CITA')
    fecha = fields.Char(string='FECHA DE CITA')
    paciente = fields.Many2one('clinica.pacientes',string='PACIENTE')
    doctor = fields.Many2one('clinica.doctores',string='DOCTOR')
    motvcita = fields.Char(string='MOTIVO DE CITA')
    tratamiento= fields.Many2one('clinica.medicamentos',string='MEDICAMENTO')
    descripcion= fields.Char(string='DESCRIPCION DE TRATAMIENTO')
    horario = fields.Many2one('clinica.horarios',string='HORARIO DE CITA')



    _sql_constraints = [
        ('unique_citas', 'unique(ide)', 'Ya existe el registro de esta cita!')
    ]
    
  
  
    
       
