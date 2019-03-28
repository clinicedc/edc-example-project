from django.contrib import admin
from edc_model_admin.dashboard import (
    ModelAdminCrfDashboardMixin,
    ModelAdminSubjectDashboardMixin,
)

from .admin_site import example_subject_admin
from .models import (
    CrfFive,
    CrfFour,
    CrfOne,
    CrfThree,
    CrfTwo,
    CrfSix,
    SubjectRequisition,
    SubjectVisit,
    OnSchedule,
    OffSchedule,
)


@admin.register(OnSchedule, site=example_subject_admin)
class OnScheduleAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    show_save_next = False
    show_cancel = True


@admin.register(OffSchedule, site=example_subject_admin)
class OffScheduleAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    show_save_next = False
    show_cancel = True


@admin.register(SubjectVisit, site=example_subject_admin)
class SubjectVisitAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    show_save_next = False
    show_cancel = True


@admin.register(CrfOne, site=example_subject_admin)
class CrfOneAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfTwo, site=example_subject_admin)
class CrfTwoAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfThree, site=example_subject_admin)
class CrfThreeAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(SubjectRequisition, site=example_subject_admin)
class SubjectRequisitionAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfFour, site=example_subject_admin)
class CrfFourAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfFive, site=example_subject_admin)
class CrfFiveAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfSix, site=example_subject_admin)
class CrfSixAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True
