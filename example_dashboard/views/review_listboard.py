from edc_review_dashboard.views import (
    SubjectReviewListboardView as BaseSubjectReviewListboardView,
)


class SubjectReviewListboardView(BaseSubjectReviewListboardView):

    listboard_model = "example_main.subjectvisit"
    navbar_name = "edc_review_dashboard"
    navbar_selected = "review"

    def get_navbar_context_data(self, context):
        return context

    @property
    def has_view_listboard_perms(self):
        return True

    @property
    def has_view_only_my_listboard_perms(self):
        return False
