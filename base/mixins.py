from django.contrib.gis.db import models
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, Orderable
from django.conf import settings


class LockableWorkFlowDrafStateRevisionModelBaseAbstract(LockableMixin, WorkflowMixin, DraftStateMixin, RevisionMixin, Orderable):
    class Meta:
        abstract = True


class LockableRevisionOrderableModelBaseAbstract(LockableMixin, RevisionMixin, Orderable):
    class Meta:
        abstract = True


class LockableDraftStateRevisionOrderableModelBaseAbstract(LockableMixin, DraftStateMixin, RevisionMixin, Orderable):
    class Meta:
        abstract = True


class LockableRevisionModelBaseAbstract(LockableMixin, RevisionMixin, Orderable):
    class Meta:
        abstract = True


LockableWorkFlowDraftStateRevisionModelBaseMixin = LockableWorkFlowDrafStateRevisionModelBaseAbstract if settings.ENABLE_MODELS_REVISIONS else Orderable
LockableRevisionOrderableModelBaseMixin = LockableRevisionOrderableModelBaseAbstract if settings.ENABLE_MODELS_REVISIONS else Orderable
LockableDraftStateRevisionOrderableModelBaseMixin = LockableDraftStateRevisionOrderableModelBaseAbstract if settings.ENABLE_MODELS_REVISIONS else Orderable
LockableRevisionModelBaseAbstract = LockableRevisionModelBaseAbstract if settings.ENABLE_MODELS_REVISIONS else Orderable
