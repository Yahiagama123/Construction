import frappe
from construction.doctype.dismissal_notice.dismissal_notice import Dismissalnotice
from frappe.model.document import Document

class yahia(Document):
    def validate(self):
        frappe.throw('This is an Error Message')
        return