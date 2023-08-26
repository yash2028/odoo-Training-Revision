from odoo import fields, models, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    import_quote_status = fields.Selection([
        ('import_quote_requested', 'Import Quote Requested'),
        ('import_quote_ready', 'Import Quote ready'),
        ('import_quote_submitted', 'Import Quote Submitted'),
        ('import_quote_revision_requested', 'Import Quote Revision Requested')
    ], string="Import Quote Status")

    domestic_quote_status = fields.Selection([
        ('domestic_quote_requested', 'Domestic Quote Requested'),
        ('domestic_quote_ready', 'Domestic Quote ready'),
        ('domestic_quote_submitted', 'Domestic Quote Submitted'),
        ('domestic_quote_revision_requested', 'Domestic Quote Revision Requested')
    ], string="Domestic Quote Status")

    def write(self, vals):
        print('\n\n\n\n\n')
        stage_id = self.env['crm.stage'].search([
            ('is_quote_ready_stage', '=', 't'),
        ])
        quote_ready_stage_id = self.env['crm.stage'].search([
            ('name', '=', 'Quote Ready'),
        ])
        print(len(stage_id), '\n\n\n')
        value1 = vals.get('domestic_quote_status') == 'domestic_quote_ready'
        value2 = vals.get('import_quote_status') == 'import_quote_ready'

        if value1 and not vals.get('import_quote_status') and len(stage_id) > 0:
            vals['stage_id'] = stage_id[0].id
        elif value1 and value2 and len(stage_id) > 0:
            vals['stage_id'] = stage_id[0].id
        elif value2 and not vals.get('domestic_quote_status') and len(stage_id) > 0:
            vals['stage_id'] = quote_ready_stage_id[0].id

        return super().write(vals)


class crm_stage(models.Model):
    _inherit = 'crm.stage'

    is_quote_ready_stage = fields.Boolean(string='Is Quote Ready Stage')
