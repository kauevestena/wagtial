from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon

# Register your serializers here.


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class PointGeoFeatureSerializer(GeoFeatureModelSerializer):
    feature_ptr = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Point
        geo_field = 'geom'
        fields = '__all__'
        # extra_fields = ['feature_ptr']

    """
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(PointGeoFeatureSerializer, self).get_field_names(declared_fields, info)
        if hasattr(self.Meta, 'extra_fields'):
            expanded_fields += self.Meta.extra_fields
        return expanded_fields
    """


class LineStringGeoFeatureSerializer(GeoFeatureModelSerializer):
    feature_ptr = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = LineString
        geo_field = 'geom'
        fields = '__all__'


class PolygonGeoFeatureSerializer(GeoFeatureModelSerializer):
    feature_ptr = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Polygon
        geo_field = 'geom'
        fields = '__all__'


class MultiPointGeoFeatureSerializer(GeoFeatureModelSerializer):
    feature_ptr = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MultiPoint
        geo_field = 'geom'
        fields = '__all__'


class MultiLineStringGeoFeatureSerializer(GeoFeatureModelSerializer):
    feature_ptr = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MultiLineString
        geo_field = 'geom'
        fields = '__all__'


class MultiPolygonGeoFeatureSerializer(GeoFeatureModelSerializer):
    feature_ptr = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MultiPolygon
        geo_field = 'geom'
        fields = '__all__'
