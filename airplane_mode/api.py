import frappe
from frappe.utils import nowdate, formatdate
# from frappe.core.doctype.communication.email import make

def update_shop_counts(doc, method):
    # Get the airport linked to the shop
    airport_name = doc.airport

    # Calculate total and occupied shops
    total_shops = frappe.db.count('Shop', filters={'airport': airport_name})
    occupied_shops = frappe.db.count('Shop', filters={'airport': airport_name, 'status': 'Occupied'})
    available_shops = frappe.db.count('Shop', filters={'airport': airport_name, 'status': 'Available'})

    # Update the total and occupied shop counts in the Airports doctype
    frappe.db.set_value('Airports', airport_name, 'total_shops', total_shops)
    frappe.db.set_value('Airports', airport_name, 'occupied_shops', occupied_shops)
    frappe.db.set_value('Airports', airport_name, 'available_shops', available_shops)
