from odoo import models, fields


class Candidate(models.Model):
    _name = "candidate.interview"
    _description = "Candidate Interview"

    name = fields.Char(
        string="Candidate Name",
        required=True
    )