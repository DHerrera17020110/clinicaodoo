# -*- coding: utf-8 -*-
from odoo import models,fields

class pacientes(models.Model):
    _name = 'clinica.pacientes'

    name = fields.Char(string='Nombre del Paciente')
    id_paciente = fields.Char(string='clave paciente')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    blood = fields.Char(string='Tipo de Sangre')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')
    alergias = fields.Char(string='Enfermedades Cronicas / Alergias')
    afiliacion = fields.Selection([('IMSS','Imss'),('ISSSTE','Issste'),('No','Ninguno')],string='Afiliado?')
    fnacimiento = fields.Char(string='Fecha de Nacimiento')
   # carrera_id = fields.Many2one('escolares.carreras',string="Carrera")

    _sql_constraints = [
        ('unique_paciente', 'unique (nombre)', 'El paciente ya existe!')
    ]

