from odoo import models, fields


class Candidate(models.Model):
    _name = "candidate.interview"
    _description = "Candidate Interview"

    name = fields.Char(
        string="Candidate Name",
        required=True
    )

    email = fields.Char(
        string="Email"
    )

    phone = fields.Char(
        string="Phone Number"
    )

    position = fields.Char(
        string="Position Applied"
    )

    experience = fields.Integer(
        string="Years of Experience"
    )

    expected_salary = fields.Float(
        string="Expected Salary"
    )

    interview_date = fields.Date(
        string="Interview Date"
    )

    interview_time = fields.Datetime(
        string="Interview Time"
    )

    notes = fields.Text(
        string="HR Notes"
    )

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("screening", "Screening"),
            ("interview", "Interview"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
        string="Status",
        default="draft"
    )