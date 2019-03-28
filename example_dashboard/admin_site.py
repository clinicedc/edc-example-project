from django.contrib.admin import AdminSite


class ExampleDashboardAdminSite(AdminSite):
    site_header = "Example Dashboard"
    site_title = "Example Dashboard"
    index_title = "Example Dashboard Administration"
    site_url = "/administration/"


example_dashboard_admin = ExampleDashboardAdminSite(
    name="example_dashboard_admin")
# example_main_admin.disable_action("delete")
