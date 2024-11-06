# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    # Define columns for the report
    columns = [
        {
            "fieldname": "airline",
            "label": "Airline",
            "fieldtype": "Link",
            "options": "Airline",
        },
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "options": "AED"
        },
    ]

    # Fetch the data from 'Airplane Ticket' with grouping by airline
    data = frappe.db.sql("""
        SELECT
            airplane.airline AS airline,
            SUM(total_amount) AS total_revenue
        FROM
            `tabAirplane Ticket` AS ticket
        JOIN
            `tabAirplane` AS airplane ON airplane.name = ticket.airplane
        WHERE
            ticket.docstatus = 1
        GROUP BY
            airplane.airline
    """, as_dict=True)

    # Create the donut chart for the report (without total in chart)
    chart = {
        "data": {
            "labels": [x["airline"] for x in data],  # No "Total" here
            "datasets": [{"values": [x["total_revenue"] for x in data]}],
        },
        "type": "donut"
    }

    # Calculate the total revenue across all airlines for report summary
    total_revenue_sum = sum([x["total_revenue"] for x in data])

    # Add a message to show the total revenue at the top
    report_summary = [
        {
            "value": total_revenue_sum,
            "label": "Total Revenue",
            "datatype": "Currency",
            "currency": "AED"
        }
    ]

    return columns, data, None, chart, report_summary



