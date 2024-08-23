// Copyright (c) 2024, AMYA and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by Make"] = {
	"filters": [
		{
			"fieldname": "vehicle",
			"label": "Vehicle",
			"fieldtype": "Link",
			"options": "Vehicle"
		}
	]
};
