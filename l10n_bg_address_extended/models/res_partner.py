# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _

import logging

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = ['res.partner']

    street_building_number = fields.Char('Building Number', compute='_compute_l10n_bg_street_data',
                                         inverse='_inverse_l10n_bg_street_data', store=True, translate=True)
    street_floor_number = fields.Char('Floor Number', compute='_compute_l10n_bg_street_data',
                                      inverse='_inverse_l10n_bg_street_data', store=True, translate=True)
    street_sector_number = fields.Char('Sector Name/Number', compute='_compute_l10n_bg_street_data',
                                       inverse='_inverse_l10n_bg_street_data', store=True, translate=True)

    def _inverse_l10n_bg_street_data(self):
        """ update self.street based on street_name, street_number and street_number2 """
        for partner in self:
            street = ((partner.street_name or '') + " " + (partner.street_number or '')).strip()
            if partner.street_sector_number:
                street = _("Sector: ") + partner.street_sector_number + ", " + street
            if partner.street_building_number:
                street = street + _(", building: ") + partner.street_building_number
            if partner.street_floor_number:
                street = street + _(", Floor: ") + partner.street_floor_number + ", " + partner.street_number2
            partner.street = street

    @api.depends('street')
    def _compute_l10n_bg_street_data(self):
        """Splits street value into sub-fields.
        Recomputes the fields of STREET_FIELDS when `street` of a partner is updated"""
        for partner in self:
            partner.update(tools.street_split(partner.street))

    def _get_street_split(self):
        self.ensure_one()
        res = super()._get_street_split()
        res.update({
            'street_building_number': self.street_building_number,
            'street_floor_number': self.street_floor_number,
            'street_sector_number': self.street_sector_number,
        })
        return res
