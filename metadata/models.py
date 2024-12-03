from django.contrib.gis.db import models
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from base.fields import GeoKnotTextField
from django.utils import timezone
import re
import html
from django.utils.html import strip_tags

# Create your models here.


class ResourceMetadataTopicCategory(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Topic categories for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataDateType(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Date types for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataMaintenanceFrequency(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Maintenance frequencies for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataRegion(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Regions for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataRestrictionCodeType(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Restriction code types for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataLicense(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Licenses for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataLanguage(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Languages for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataSpatialRepresentationType(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    """
    Spatial representation types for dataset metadata.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ResourceMetadataBaseMixin(models.Model):
    """
    Base class for resource metadata.
    """

    abstract = GeoKnotTextField(null=True, blank=True)
    purpose = GeoKnotTextField(null=True, blank=True)
    topic_category = models.ForeignKey(ResourceMetadataTopicCategory, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    date_type = models.ForeignKey(ResourceMetadataDateType, on_delete=models.PROTECT, null=True, blank=True)
    edition = models.CharField(max_length=255, null=True, blank=True)
    attribution = models.CharField(max_length=255, null=True, blank=True)
    doi = models.URLField(null=True, blank=True)
    maintenance_frequency = models.ForeignKey(ResourceMetadataMaintenanceFrequency, on_delete=models.PROTECT, null=True, blank=True)
    regions = models.ManyToManyField(ResourceMetadataRegion, blank=True)
    restriction_code_type = models.ForeignKey(ResourceMetadataRestrictionCodeType, on_delete=models.PROTECT, null=True, blank=True)
    other_constraints = GeoKnotTextField(null=True, blank=True)
    license = models.ForeignKey(ResourceMetadataLicense, on_delete=models.PROTECT, null=True, blank=True)
    language = models.ForeignKey(ResourceMetadataLanguage, on_delete=models.PROTECT, null=True, blank=True)
    spatial_representation_type = models.ForeignKey(ResourceMetadataSpatialRepresentationType, on_delete=models.PROTECT, null=True, blank=True)
    supplemental_information = GeoKnotTextField(null=True, blank=True)
    data_quality_statement = GeoKnotTextField(null=True, blank=True)

    @property
    def temporal_extent_start(self):
        return "TODO: devolver el minimo de las fechas de los recursos relacionados"

    @property
    def temporal_extent_end(self):
        return "TODO: devolver el maximo de las fechas de los recursos relacionados"

    @property
    def bbox(self):
        return "TODO: devolver el bbox de los recursos relacionados"

    @staticmethod
    def _remove_html_tags(attribute_str):
        _attribute_str = attribute_str
        try:
            pattern = re.compile("<.*?>")
            _attribute_str = html.unescape(
                re.sub(pattern, "", attribute_str).replace("\n", " ").replace("\r", "").strip()
            )
        except Exception:
            if attribute_str:
                _attribute_str = html.unescape(attribute_str.replace("\n", " ").replace("\r", "").strip())
        return strip_tags(_attribute_str)

    class Meta:
        abstract = True
