from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Candidate(models.Model):
    _name = "candidate.interview"
    _description = "Candidate Interview"

    candidate_code = fields.Char(
        string="Candidate ID",
        required=True,
        copy=False,
        readonly=True,
        default="New"
    )

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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("candidate_code", "New") == "New":
                vals["candidate_code"] = self.env["ir.sequence"].next_by_code(
                    "candidate.interview"
                ) or "New"

        return super().create(vals_list)
    
    # =========================
    # Button Actions
    # =========================

    def action_screening(self):
        self.write({"status": "screening"})

    def action_interview(self):
        self.write({"status": "interview"})

    def action_accept(self):
        self.write({"status": "accepted"})

    def action_reject(self):
        self.write({"status": "rejected"})

    # =========================
    # Validation
    # =========================

    @api.constrains("expected_salary")
    def _check_expected_salary(self):
        for record in self:
            if record.expected_salary < 0:
                raise ValidationError(
                    "Expected Salary cannot be negative."
                )

    @api.constrains("experience")
    def _check_experience(self):
        for record in self:
            if record.experience < 0:
                raise ValidationError(
                    "Years of Experience cannot be negative."
                )