# -*- coding: utf-8 -*-
from odoo import models,fields

class doctores(models.Model):
    _name = 'clinica.doctores'

    name = fields.Char(string='Nombre del doctor')
    id_doctor = fields.Char(string='Cedula profecional')
    especialidad = fields.Char(string='Especialidad')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')
    horario_id = fields.Many2one('clinica.horarios',string='Horarios')
    email = fields.Char(string='Email')


    _sql_constraints = [
        ('unique_doctores', 'unique (name)', 'El Doctor ya existe!')
    ]

