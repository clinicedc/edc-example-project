from edc_dashboard.views import ListboardView as BaseListboardView


class SubjectListboardView(BaseListboardView):

    listboard_model = "example_main.subjectvisit"
    navbar_name = "subject_listboard"
    navbar_selected = "subjects"

    def get_navbar_context_data(self, context):
        return context

    @property
    def has_view_listboard_perms(self):
        return True

    @property
    def has_view_only_my_listboard_perms(self):
        return False
