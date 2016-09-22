# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
#    Copyright 2016 Niboo SPRL
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'HR - Holiday On Timesheet',
    'category': 'HR',
    'summary': "Timesheet shows employee's holidays",
    'website': '',
    'version': '9.1.0',
    'description': """
    When a leave is approved, this module create analytic lines for the holidays to appear in the timesheet
        """,
    'author': 'Niboo',
    'depends': [
        'hr_timesheet',
        'hr_timesheet_sheet',
        'hr_holidays',
    ],
    'data': [
        'data/holiday_account.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}