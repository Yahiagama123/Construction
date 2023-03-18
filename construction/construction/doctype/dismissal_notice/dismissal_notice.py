# Copyright (c) 2023, ahia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt
class Dismissalnotice(Document):

	@frappe.whitelist()
	def validate(doc, method=None):
	
	
			
			doc.total = 00
			doc.tqty=00
			for x in doc.list:
				doc.total += flt(x.sell_price)
				doc.tqty += flt(x.qty)
				
				if doc.tqty == 0:
					#doc.total_price=200
					frappe.throw(('Please Enter Quantity Of Items'))
					return
				
				if x.qty > x.qty_exist:
					frappe.throw(('Please Enter Exist Quantity Of Items'))
					return