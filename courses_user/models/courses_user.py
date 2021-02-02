# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Courses_course(models.Model):
    _name = 'courses.course'
    _inherit = ['courses.course','mail.thread']

    professor = fields.Many2one('res.users', 'Professor')

    link = fields.Char('Link')
    discount = fields.Float('Discount(%)', required=True)
    
    total_iva = fields.Float('Total Price with IVA applied', compute="_totalIva", store=True)
    total_discount = fields.Float('Total Price with discount applied', compute="_totalDesc", store=True)
    
    @api.depends('total','discount')
    def _totalDesc(self):
        for r in self:
            r.total_discount =   r.total - (r.total * r.discount / 100)

    @api.depends('total_discount')
    def _totalIva(self):
        for r in self:
            r.total_iva = r.total_discount*0.21 + r.total_discount


