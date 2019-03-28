import uuid

from django.db import models
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_lab.model_mixins import RequisitionModelMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_model.models import BaseUuidModel
from edc_reference.model_mixins import ReferenceModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_sites.models import SiteModelMixin
from edc_visit_schedule.model_mixins import OnScheduleModelMixin, OffScheduleModelMixin
from edc_visit_tracking.model_mixins import CrfModelMixin, VisitModelMixin
from edc_consent.field_mixins.identity_fields_mixin import IdentityFieldsMixin


class OnSchedule(OnScheduleModelMixin, BaseUuidModel):

    pass


class OffSchedule(OffScheduleModelMixin, BaseUuidModel):

    pass


class DeathReport(UniqueSubjectIdentifierFieldMixin, SiteModelMixin, BaseUuidModel):

    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.subject_identifier,)


class SubjectConsent(
    ConsentModelMixin,
    PersonalFieldsMixin,
    IdentityFieldsMixin,
    UniqueSubjectIdentifierFieldMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    SiteModelMixin,
    BaseUuidModel,
):

    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.subject_identifier,)


class SubjectVisit(
    VisitModelMixin,
    ReferenceModelMixin,
    CreatesMetadataModelMixin,
    SiteModelMixin,
    BaseUuidModel,
):

    pass


class SubjectRequisition(RequisitionModelMixin, BaseUuidModel):

    pass


class BaseCrfModel(CrfModelMixin, SiteModelMixin, models.Model):

    f1 = models.CharField(max_length=50, default=uuid.uuid4)

    class Meta:
        abstract = True


class CrfOne(BaseCrfModel, BaseUuidModel):
    pass


class CrfTwo(BaseCrfModel, BaseUuidModel):

    pass


class CrfThree(BaseCrfModel, BaseUuidModel):

    pass


class CrfFour(BaseCrfModel, BaseUuidModel):

    pass


class CrfFive(BaseCrfModel, BaseUuidModel):

    pass


class CrfSix(BaseCrfModel, BaseUuidModel):

    pass


class CrfSeven(BaseCrfModel, BaseUuidModel):

    pass
