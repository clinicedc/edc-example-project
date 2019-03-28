from django.contrib.admin import AdminSite


class ExampleSubjectAdminSite(AdminSite):
    site_header = "Example Subject"
    site_title = "Example Subject"
    index_title = "Example Subject Administration"
    site_url = "/administration/"


example_subject_admin = ExampleSubjectAdminSite(
    name="example_subject_admin")
# example_main_admin.disable_action("delete")
