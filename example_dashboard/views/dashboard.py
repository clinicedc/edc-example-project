from edc_subject_dashboard.views import SubjectDashboardView as BaseSubjectDashboardView


class SubjectDashboardView(BaseSubjectDashboardView):

    consent_model = "example_main.subjectconsent"
    navbar_name = "subject_dashboard"
    visit_model = "example_main.subjectvisit"

    def get_navbar_context_data(self, context):
        return context
