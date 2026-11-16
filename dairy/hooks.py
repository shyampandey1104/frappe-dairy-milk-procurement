# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "dairy"
app_title = "Frappe Dairy Milk Procurement"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Dairy Milk Procurement for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/dairy/css/dairy.bundle.css"
app_include_js = "/assets/dairy/js/dairy.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "dairy.engine.on_document_submit",
        "on_cancel": "dairy.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "dairy.engine.daily_scheduled_sync"
    ]
}
