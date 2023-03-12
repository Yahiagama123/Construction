// Copyright (c) 2023, ahia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Construction", {
    excoast:function(frm,cdt,cdn){
        
        const row = locals[cdt][cdn];
        if(row.excoast!==undefined){
            frappe.model.set_value(cdt, cdn, "exprofit", row.price-row.excoast);
   
        }
    }
});




frappe.ui.form.on("Construction", {
    excoast:function(frm,cdt,cdn){
        
        const row = locals[cdt][cdn];
        if(row.excoast!==undefined){
            frappe.model.set_value(cdt, cdn, "preprofit", (row.exprofit/row.excoast)*100);
        }
    }
});
