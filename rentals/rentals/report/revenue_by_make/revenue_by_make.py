# Copyright (c) 2024, AMYA and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname": "make",
			"label": "Make",
			"fieldtype": "Data"
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"options": "USD"
		}
	]
	data_filters = {
		"docstatus": 1
	}

	if filters.vehicle:
		data_filters.update({
			"vehicle": filters.vehicle
		})
	data = frappe.get_all(
		"Ride Booking", 
		fields=[
			"SUM(total_amount) as total_revenue", 
			"vehicle.make"
		], 
		filters=data_filters, 
		group_by="make"
	)

	chart_data = {
		"labels": [d.make for d in data],
		"datasets": [
			{
				"values": [d.total_revenue for d in data]
			}
		],
	}

	chart = {
		"title": "Revenue by Make",
		"data": chart_data,
		"type": "pie"
	}

	return columns, data, None, chart
