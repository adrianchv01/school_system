# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api


class School(models.Model):
    _name = 'school.subject'
    _description = 'School management'

    name = fields.Char(string='Name', required=True)
    credits = fields.Integer(string="Credits", required=True)
    active = fields.Boolean(string='Active')
    max_students = fields.Integer(String="Students", required=True)


class Student(models.Model):
    _name = 'school.student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    birth_date = fields.date(string='Date', required=True)
    final_exam_grade = fields.Float(string='Final Exam')


class Teacher(models.Model):
    _name = 'school.teacher'

    name = fields.Char(string='Name', required=True)
    profile = fields.Text(string='Profile')
