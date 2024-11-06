// Copyright (c) 2024, kusum and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh: function(frm) {
        // Add a custom button to open a dialog for seat number input
        frm.add_custom_button('Assign Seat', function() {
            // Create a dialog to input seat number
            let d = new frappe.ui.Dialog({
                title: 'Select Seat',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Submit',
                primary_action(values) {
                    // Set the seat number in the Seat field
                    frm.set_value('seat', values.seat_number);
                    // Close the dialog after submission
                    d.hide();
                }
            });
            
            // Show the dialog
            d.show();
        });
    }

        
});

