# -*- coding: utf-8 -*-
# Copyright (c) 2024, [Your Name] and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class BookTransaction(Document):
    def validate(self):
        """Validate transaction data"""
        
        # Validation 1: If Issue, due_date is mandatory
        if self.transaction_type == "Issue":
            if not self.due_date:
                frappe.throw("Due Date is mandatory for Issue transactions")
        
        # Validation 2: If Return, return_date is mandatory
        if self.transaction_type == "Return":
            if not self.return_date:
                frappe.throw("Return Date is mandatory for Return transactions")
        
        # Validation 3: return_date cannot be before transaction_date
        if self.return_date:
            if getdate(self.return_date) < getdate(self.transaction_date):
                frappe.throw("Return Date cannot be before Transaction Date")