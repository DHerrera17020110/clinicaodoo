# -*- coding: utf-8 -*-
from odoo import models
from datetime import *

class receta(models.AbstractModel):
    _name = 'report.receta'

    def render_html(self, data=None):

        report_obj = self.env['report']
        report = report_obj._get_report_from_name('clinica.receta')

        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(self._ids),
        }

        
        return report_obj.render('clinica.receta', docargs)