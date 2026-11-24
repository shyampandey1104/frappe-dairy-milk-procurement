# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "dairy"
app_title = "Frappe Dairy Milk Procurement"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Dairy Milk Procurement - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/dairy/css/dairy.bundle.css"
app_include_js = "/assets/dairy/js/dairy.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Dairy Milk Procurement Entry": {
        "validate": "dairy.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "dairy.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "dairy.tasks.hourly_sync"
    ],
    "daily": [
        "dairy.tasks.daily_reconciliation"
    ],
    "weekly": [
        "dairy.tasks.weekly_digest"
    ]
}
