from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (Resource, PointVectorLayer)
# from .models import (Resource, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer, GeometryCollectionVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS)
from features.serializers import PointGeoFeatureSerializer
# from features.serializers import PointGeoFeatureSerializer, LineStringGeoFeatureSerializer, PolygonGeoFeatureSerializer, MultiPointGeoFeatureSerializer, MultiLineStringGeoFeatureSerializer, MultiPolygonGeoFeatureSerializer, GeometryCollectionGeoFeatureSerializer


# Register your models here.


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = '__all__'


class PointVectorLayerSerializer(serializers.ModelSerializer):
    features = PointGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = PointVectorLayer
        fields = '__all__'


"""
class LineStringVectorLayerSerializer(serializers.ModelSerializer):
    lines = LineStringGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = LineStringVectorLayer
        fields = '__all__'


class PolygonVectorLayerSerializer(serializers.ModelSerializer):
    polygons = PolygonGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = PolygonVectorLayer
        fields = '__all__'


class MultiPointVectorLayerSerializer(serializers.ModelSerializer):
    multipoints = MultiPointGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = MultiPointVectorLayer
        fields = '__all__'


class MultiLineStringVectorLayerSerializer(serializers.ModelSerializer):
    multilines = MultiLineStringGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = MultiLineStringVectorLayer
        fields = '__all__'


class MultiPolygonVectorLayerSerializer(serializers.ModelSerializer):
    multipolygons = MultiPolygonGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = MultiPolygonVectorLayer
        fields = '__all__'


class GeometryCollectionVectorLayerSerializer(serializers.ModelSerializer):
    geometrycollections = GeometryCollectionGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = GeometryCollectionVectorLayer
        fields = '__all__'


class RasterLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RasterLayer
        fields = '__all__'


class DataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = '__all__'


class RemoteWMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteWMS
        fields = '__all__'


class RemoteWFSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteWFS
        fields = '__all__'


# GeoFeatureModelSerializer
"""
