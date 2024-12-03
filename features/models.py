from django.conf import settings
from django.contrib.gis.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, Orderable
from modelcluster.fields import ParentalKey
from resources.models import (VectorLayer, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer,
                              MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer,
                              GeometryCollectionVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS)
from polymorphic.models import PolymorphicModel
from .documents import PointFeatureDocument, LineStringFeatureDocument, PolygonFeatureDocument
from django.forms.models import model_to_dict
import json
from django.utils.dateformat import format


# Create your models here.


class Feature(PolymorphicModel, LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


class Point(Feature):
    geom = models.PointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourcePointsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.title}: {self.id}"

    @receiver(post_save, sender='features.Point')
    def index_point_feature(sender, instance, **kwargs):
        if not instance.has_unpublished_changes:
            geom_geojson = json.loads(instance.geom.geojson)

            print("instance.data", instance.data)

            # Convert the instance to a dictionary and remove 'id' and 'geom'
            properties = {
                'data': instance.data,
                'layer': instance.layer.id}


            doc = PointFeatureDocument(
                meta={'id': instance.id},
                properties=properties,
                layer=instance.layer.id,
                geom=geom_geojson,
                last_published_at=instance.last_published_at
            )
            print("Properties: ", properties)

            print("Document: ", doc)
            doc.save()

    class Meta:
        verbose_name = "Point"
        verbose_name_plural = "Points"


class LineString(Feature):
    geom = models.LineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceLineStringsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.title}: {self.id}"

    @receiver(post_save, sender='features.LineString')
    def index_linestring_feature(sender, instance, **kwargs):
        if not instance.has_unpublished_changes:
            # geom_3857 = instance.geom.transform(3857, clone=True)
            geom_geojson = json.loads(instance.geom.geojson)

            # Convert the instance to a dictionary and remove 'id' and 'geom'
            properties = model_to_dict(instance)
            properties.pop('id', None)
            properties.pop('geom', None)

            doc = LineStringFeatureDocument(
                meta={'id': instance.id},
                properties=properties,
                layer=instance.layer.id,
                geom=geom_geojson,
                last_published_at=instance.last_published_at
            )
            doc.save()

    class Meta:
        verbose_name = "LineString"
        verbose_name_plural = "LineStrings"


class Polygon(Feature):
    geom = models.PolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourcePolygonsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.title}: {self.id}"

    @receiver(post_save, sender='features.Polygon')
    def index_polygon_feature(sender, instance, **kwargs):
        if not instance.has_unpublished_changes:
            # geom_3857 = instance.geom.transform(3857, clone=True)
            geom_geojson = json.loads(instance.geom.geojson)

            # Convert the instance to a dictionary and remove 'id' and 'geom'
            properties = model_to_dict(instance)
            properties.pop('id', None)
            properties.pop('geom', None)

            doc = PolygonFeatureDocument(
                meta={'id': instance.id},
                properties=properties,
                layer=instance.layer.id,
                geom=geom_geojson,
                last_published_at=instance.last_published_at
            )
            doc.save()

    class Meta:
        verbose_name = "Polygon"
        verbose_name_plural = "Polygons"


class MultiPoint(Feature):
    geom = models.MultiPointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceMultiPointsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.title}: {self.id}"


class MultiLineString(Feature):
    geom = models.MultiLineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceMultiLineStringsFile", on_delete=models.CASCADE, null=True,
                              blank=True)

    def __str__(self):
        return f"{self.layer.title}: {self.id}"


class MultiPolygon(Feature):
    geom = models.MultiPolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceMultiPolygonsFile", on_delete=models.CASCADE, null=True,
                              blank=True)

    def __str__(self):
        return f"{self.layer.title}: {self.id}"
