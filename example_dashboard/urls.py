
from .views import (
    SubjectDashboardView,
    SubjectListboardView,
    SubjectReviewListboardView,
)

app_name = "example_dashboard"


urlpatterns = SubjectDashboardView.urls(namespace=app_name, label="dashboard")
urlpatterns += SubjectListboardView.urls(namespace=app_name, label="listboard")
urlpatterns += SubjectReviewListboardView.urls(
    namespace=app_name, label="review")
