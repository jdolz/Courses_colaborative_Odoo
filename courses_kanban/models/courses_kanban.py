#-*- coding: utf-8 -*-
from odoo import models, fields
class Courses_course(models.Model):
    _inherit = 'courses.course'

    recommended = fields.Selection([('0','Not'),('1','Not too much'),('2','Not much'),('3','Normaly'),('4','A Bit'),('5','Highly')],'Recommended',default='0')
    
    
    kanban_state = fields.Selection([('normal', 'Not ready'),('blocked', 'Already finished'),('done', 'Currently coursing')],'Kanban State', default='normal')



    

