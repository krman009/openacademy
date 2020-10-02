# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy_course'

    image = fields.Binary()
    name = fields.Char(string='Title', help='This is title for your course', required=True)
    description = fields.Text(copy=False)
    rich_description = fields.Html()
    responsibe_id = fields.Many2one('res.users',ondelete="cascade")
    session_ids = fields.One2many('openacademy.session', 'course_id')
