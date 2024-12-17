# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

import random
import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		total_add_ons = 0
		valid_add_ons = []
		add_on_items = set()

		if self.add_ons:
			
			for add_on in self.add_ons:
				if add_on.item not in add_on_items:
					add_on_items.add(add_on.item)
					valid_add_ons.append(add_on)
					total_add_ons += add_on.amount

		self.add_ons = valid_add_ons
		self.total_amount = self.flight_price + total_add_ons		

		self.validate_capacity()

	def before_submit(self):
		if self.docstatus == 1 and self.status != "Boarded":
			frappe.throw("Cannot submit the Airplane Ticket. Status must be 'Boarded' to proceed.")


	def before_insert(self):
		random_integer = random.randint(1, 99)
		random_alphabet = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{random_integer}{random_alphabet}"

		random_integers = random.randint(1, 5)
		random_alphabets = random.choice(['Gate'])
		self.gate = f"{random_integers} {random_alphabets}"
	


	def validate_capacity(self):
		airplane = frappe.get_doc('Airplane', self.airplane)
		total_tickets = frappe.db.count('Airplane Ticket', {'airplane': self.airplane})
		if total_tickets >= airplane.capacity:
			frappe.throw(f"Cannot issue more tickets! Airplane capacity of {airplane.capacity} is full.")

	