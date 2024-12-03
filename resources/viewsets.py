from rest_framework import viewsets
from .models import (Resource, PointVectorLayer)
"""
from .models import (Resource, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer,
                     MultiLineStringVectorLayer, MultiPolygonVectorLayer, GeometryCollectionVectorLayer,
                     RasterLayer, DataTable, RemoteWMS, RemoteWFS)
"""
from .serializers import (ResourceSerializer, PointVectorLayerSerializer)
"""
from .serializers import (ResourceSerializer, PointVectorLayerSerializer, LineStringVectorLayerSerializer,
                          PolygonVectorLayerSerializer, MultiPointVectorLayerSerializer, MultiLineStringVectorLayerSerializer,
                          MultiPolygonVectorLayerSerializer, GeometryCollectionVectorLayerSerializer,
                          RasterLayerSerializer, DataTableSerializer,
                          RemoteWMSSerializer, RemoteWFSSerializer)
"""

# Register your models here.


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class PointVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = PointVectorLayer.objects.all()
    serializer_class = PointVectorLayerSerializer

"""
class LineStringVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = LineStringVectorLayer.objects.all()
    serializer_class = LineStringVectorLayerSerializer


class PolygonVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = PolygonVectorLayer.objects.all()
    serializer_class = PolygonVectorLayerSerializer


class MultiPointVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = MultiPointVectorLayer.objects.all()
    serializer_class = MultiPointVectorLayerSerializer


class MultiLineStringVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = MultiLineStringVectorLayer.objects.all()
    serializer_class = MultiLineStringVectorLayerSerializer


class MultiPolygonVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = MultiPolygonVectorLayer.objects.all()
    serializer_class = MultiPolygonVectorLayerSerializer


class GeometryCollectionVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = GeometryCollectionVectorLayer.objects.all()
    serializer_class = GeometryCollectionVectorLayerSerializer


class RasterLayerViewSet(viewsets.ModelViewSet):
    queryset = RasterLayer.objects.all()
    serializer_class = RasterLayerSerializer


class DataTableViewSet(viewsets.ModelViewSet):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer


class RemoteWMSViewSet(viewsets.ModelViewSet):
    queryset = RemoteWMS.objects.all()
    serializer_class = RemoteWMSSerializer


class RemoteWFSViewSet(viewsets.ModelViewSet):
    queryset = RemoteWFS.objects.all()
    serializer_class = RemoteWFSSerializer
"""