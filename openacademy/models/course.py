# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy_course'

    image = fields.Binary(string='Course Image')
    name = fields.Char(string='Title', help='This is the title for your course', required=True)
    description = fields.Text(copy=False, string='Description')
    rich_description = fields.Html()
    responsible_id = fields.Many2one('res.users', string='Responsible', ondelete="cascade")
    session_ids = fields.One2many('openacademy.session', 'course_id')


    def unlink(self):
        for course in self:
            if course.name in ['networking', 'it']:
                raise UserError(_('You cannot delete a Course.'))
        return super(Course, self).unlink()
