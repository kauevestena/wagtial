from django.contrib.gis.db import models
import uuid
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from base.fields import GeoKnotTextField
from polymorphic.models import PolymorphicModel
from .managers import ResourceBaseManager
from metadata.models import ResourceMetadataBaseMixin
from resource_attributes.models import ResourceCategory
from autoslug import AutoSlugField
from base import enumerations
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


def is_resourcecategory_live(pk):
    if not ResourceCategory.objects.filter(pk=pk, live=True).exists():
        raise ValidationError('The resource category must be live.')


class ResourceBaseAbstract(LockableWorkFlowDraftStateRevisionModelBaseMixin, ClusterableModel, ResourceMetadataBaseMixin):
    """
    Base model for all resources.
    """

    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True, editable=False)
    description = GeoKnotTextField(null=True, blank=True)
    category = models.ForeignKey(ResourceCategory, on_delete=models.PROTECT)
    tags = TaggableManager(help_text=None, blank=True, verbose_name=_("tags"))
    is_featured = models.BooleanField(default=False)
    is_advertised = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='resources/thumbnails/', null=True, blank=True)
    popular_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title



    class Meta:
        abstract = True


class ResourceRemoteServiceMixin(models.Model):
    """
    Mixin for resources that have a remote URL.
    """

    service_type = models.CharField(max_length=255, choices=enumerations.REMOTE_SERVICE_TYPES, default='wms')
    service_url = models.URLField()

    class Meta:
        abstract = True


class Resource(PolymorphicModel, ResourceBaseAbstract):
    """
    A resource.
    """
    index_name = models.CharField(max_length=255, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.polymorphic_ctype and self.polymorphic_ctype.model:
            self.index_name = self.polymorphic_ctype.model
        super().save(*args, **kwargs)

    @receiver(post_save, sender='resources.Resource')
    def update_index_name(sender, instance, **kwargs):
        instance.index_name = instance.polymorphic_ctype.model
        instance.save()

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"


class VectorLayer(Resource):
    """
    A dataset.
    """

    class Meta:
        verbose_name = "Vector Layer"
        verbose_name_plural = "Vector Layers"


class PointVectorLayer(VectorLayer):
    """
    A point dataset.
    """

    class Meta:
        verbose_name = "Point Vector Layer"
        verbose_name_plural = "Resources: Point Vector Layers"


class LineStringVectorLayer(VectorLayer):
    """
    A line dataset.
    """

    class Meta:
        verbose_name = "LineString Vector Layer"
        verbose_name_plural = "Resources: LineString Vector Layers"


class PolygonVectorLayer(VectorLayer):
    """
    A polygon dataset.
    """

    class Meta:
        verbose_name = "Polygon Vector Layer"
        verbose_name_plural = "Resources: Polygon Vector Layers"


class MultiPointVectorLayer(VectorLayer):
    """
    A multipoint dataset.
    """

    class Meta:
        verbose_name = "MultiPoint Vector Layer"
        verbose_name_plural = "Resources: MultiPoint Vector Layers"


class MultiLineStringVectorLayer(VectorLayer):
    """
    A multilinestring dataset.
    """

    class Meta:
        verbose_name = "MultiLineString Vector Layer"
        verbose_name_plural = "Resources: MultiLineString Vector Layers"


class MultiPolygonVectorLayer(VectorLayer):
    """
    A multipolygon dataset.
    """

    class Meta:
        verbose_name = "MultiPolygon Vector Layer"
        verbose_name_plural = "Resources: MultiPolygon Vector Layers"


class GeometryCollectionVectorLayer(VectorLayer):
    """
    A geometry collection dataset.
    """

    class Meta:
        verbose_name = "GeometryCollection Vector Layer"
        verbose_name_plural = "Resources: GeometryCollection Vector Layers"


class RasterLayer(Resource):
    """
    A dataset.
    """

    class Meta:
        verbose_name = "Raster Layer"
        verbose_name_plural = "Resources: Raster Layers"


class DataTable(Resource):
    """
    A table.
    """

    class Meta:
        verbose_name = "Data Table"
        verbose_name_plural = "Resources: Data Tables"


class RemoteWMS(Resource, ResourceRemoteServiceMixin):
    """
    A WMS service.
    """

    class Meta:
        verbose_name = "WMS Service"
        verbose_name_plural = "Resources: WMS Services"


class RemoteWFS(Resource, ResourceRemoteServiceMixin):
    """
    A WFS service.
    """

    class Meta:
        verbose_name = "WFS Service"
        verbose_name_plural = "Resources: WFS Services"
