from django.conf import settings
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include
from django_collect_offline.admin_site import django_collect_offline_admin
from edc_action_item.admin_site import edc_action_item_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_dashboard.views import AdministrationView
from edc_export.admin_site import edc_export_admin
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_locator.admin_site import edc_locator_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_notification.admin_site import edc_notification_admin
from edc_pdutils.admin_site import edc_pdutils_admin
from edc_reference.admin_site import edc_reference_admin
from edc_registration.admin_site import edc_registration_admin
from example_subject.admin_site import example_subject_admin

from .views import HomeView

app_name = settings.APP_NAME


def handler500(request):
    """500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """

    context = {"request": request}
    template_name = "500.html"  # You need to create a 500.html template.
    return TemplateResponse(request, template_name, context, status=500)


urlpatterns = [
    path("accounts/", include("edc_auth.urls")),
    path("admin/", admin.site.urls),
    path("administration/", AdministrationView.as_view(),
         name="administration_url"),
]

for app_name in [
    "edc_auth",
    "django_collect_offline",
    "django_collect_offline_files",
    "edc_action_item",
    "edc_appointment",
    "edc_base",
    "edc_consent",
    "edc_device",
    "edc_export",
    "edc_identifier",
    "edc_lab",
    "edc_lab_dashboard",
    "edc_label",
    "edc_locator",
    "edc_metadata",
    "edc_notification",
    "edc_pdutils",
    "edc_protocol",
    "edc_reference",
    "edc_registration",
    "edc_subject_dashboard",
    "edc_visit_schedule",
]:
    urlpatterns.append(path(f"{app_name}/", include(f"{app_name}.urls")))

# admin sites
urlpatterns += [
    path("admin/", django_collect_offline_admin.urls),
    path("admin/", edc_action_item_admin.urls),
    path("admin/", edc_appointment_admin.urls),
    path("admin/", edc_export_admin.urls),
    path("admin/", edc_identifier_admin.urls),
    path("admin/", edc_lab_admin.urls),
    path("admin/", edc_locator_admin.urls),
    path("admin/", edc_metadata_admin.urls),
    path("admin/", edc_notification_admin.urls),
    path("admin/", edc_pdutils_admin.urls),
    path("admin/", edc_reference_admin.urls),
    path("admin/", edc_registration_admin.urls),
    path("admin/", example_subject_admin.urls),
]

urlpatterns += [
    path("", HomeView.as_view(), name="home_url"),
]
