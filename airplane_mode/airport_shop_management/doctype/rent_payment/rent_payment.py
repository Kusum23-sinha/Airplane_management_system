# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentPayment(Document):
    pass
	# # rent_payment.py
	# def validate(self):
	# 	# Check if the rent amount matches the shop rent
	# 	shop_rent = frappe.get_value("Shop", self.shop, "rent_amount")
	# 	if self.rent_amount != shop_rent:
	# 		frappe.throw("Rent Amount does not match the Shop's rent. Please correct it.")

