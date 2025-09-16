# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KarmaBotUser(models.Model):
    _name = 'karmabot.user'
    _description = 'KarmaBot User'
    _rec_name = 'name'

    name = fields.Char(string='Full Name', required=True)
    telegram_id = fields.Char(string='Telegram ID', required=True, index=True)
    username = fields.Char(string='Username')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    city = fields.Char(string='City')
    role = fields.Selection([
        ('user', 'User'),
        ('partner', 'Partner'),
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
    ], string='Role', default='user')
    points = fields.Integer(string='Points', default=0)
    level = fields.Integer(string='Level', default=1)
    scans_count = fields.Integer(string='Scans Count', default=0)
    referrals_count = fields.Integer(string='Referrals Count', default=0)
    is_active = fields.Boolean(string='Active', default=True)
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super(KarmaBotUser, self).create(vals)

    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super(KarmaBotUser, self).write(vals)
