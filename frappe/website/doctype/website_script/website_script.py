# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document

class WebsiteScript(Document):
		
	def on_update(self):
		"""clear cache"""
		from frappe.sessions import clear_cache
		clear_cache('Guest')

		from frappe.website.render import clear_cache
		clear_cache()