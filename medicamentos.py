# -*- coding: utf-8 -*-
from odoo import models,fields

class medicamentos(models.Model):
    _name = 'clinica.medicamentos'

    name = fields.Char(string='Nombre Medicamento')
    med_id = fields.Char(string='clave Medicamento')
    laboratorio = fields.Char(string='Laboratorio')
    cantidad = fields.Char(string='Cantidad')
    dosis = fields.Char(string='dosis')


    _sql_constraints = [
        ('unique_medicamentos', 'unique (nombre)', 'Este medicamento ya existe!')
    ]

