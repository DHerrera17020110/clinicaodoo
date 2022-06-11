# -*- coding: utf-8 -*-
{
    'name': 'Clinica',
    'version': '1.0',
    'category': 'Salud',
    'description': 'Clinica de Especialidad',
    'author': 'Daniel Herrera Cansino,Enrique Huerta Hurtado,Iridian Reyes Guzman,Oscar Arreola Virrueta',
    'maintainer': 'ITSA',
    'website': 'http://www.itsa.edu.mx',
    'depends': ['base'],
    'data': [
        'security/citas.xml',
        'security/ir.model.access.csv',
        'views/pacientes_view.xml',
        'views/citas_view.xml',
        'views/medicamentos_view.xml',
        'views/doctores_view.xml',
        'views/horarios_view.xml',
        'reports/receta.xml',
        'views/menu_view.xml',
        
    ],
    'installable': True,
    'auto_install': False,
}