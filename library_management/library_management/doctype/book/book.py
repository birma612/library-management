import frappe
from frappe.model.document import Document

class Book(Document):

    def validate(self):

        if self.total_copies is None:
            self.total_copies = 0

        if self.available_copies is None:
            self.available_copies = 0

        if self.total_copies < 0:
            frappe.throw("Total copies cannot be negative")

        if self.available_copies < 0:
            frappe.throw("Available copies cannot be negative")

        if self.available_copies > self.total_copies:
            self.available_copies = self.total_copies

    def before_save(self):
        if self.is_new():
            self.available_copies = self.total_copies