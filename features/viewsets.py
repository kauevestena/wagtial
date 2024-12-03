from rest_framework import viewsets
from .models import Point
# from .models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection
from .serializers import (PointSerializer, )
# from .serializers import (PointSerializer, LineStringSerializer, PolygonSerializer, MultiPointSerializer, MultiLineStringSerializer, MultiPolygonSerializer, GeometryCollectionSerializer)
from .serializers import (PointGeoFeatureSerializer, )
# from .serializers import (PointGeoFeatureSerializer, LineStringGeoFeatureSerializer, PolygonGeoFeatureSerializer, MultiPointGeoFeatureSerializer, MultiLineStringGeoFeatureSerializer, MultiPolygonGeoFeatureSerializer, GeometryCollectionGeoFeatureSerializer)

# Register your viewsets here.


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointGeoFeatureSerializer


"""
class LineStringViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer


class MultiPointViewSet(viewsets.ModelViewSet):
    queryset = MultiPoint.objects.all()
    serializer_class = MultiPointSerializer


class MultiLineStringViewSet(viewsets.ModelViewSet):
    queryset = MultiLineString.objects.all()
    serializer_class = MultiLineStringSerializer


class MultiPolygonViewSet(viewsets.ModelViewSet):
    queryset = MultiPolygon.objects.all()
    serializer_class = MultiPolygonSerializer


class GeometryCollectionViewSet(viewsets.ModelViewSet):
    queryset = GeometryCollection.objects.all()
    serializer_class = GeometryCollectionSerializer


# GeoFeatureModelViewSet


class PointGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointGeoFeatureSerializer


class LineStringGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringGeoFeatureSerializer


class PolygonGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonGeoFeatureSerializer


class MultiPointGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = MultiPoint.objects.all()
    serializer_class = MultiPointGeoFeatureSerializer


class MultiLineStringGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = MultiLineString.objects.all()
    serializer_class = MultiLineStringGeoFeatureSerializer


class MultiPolygonGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = MultiPolygon.objects.all()
    serializer_class = MultiPolygonGeoFeatureSerializer


class GeometryCollectionGeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = GeometryCollection.objects.all()
    serializer_class = GeometryCollectionGeoFeatureSerializer
"""