# Copyright (c) 2024, AMYA and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}".strip()

	def send_alert(self):
		print("Sending Message...")
