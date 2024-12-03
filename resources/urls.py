from django.urls import path
from .viewsets import (ResourceViewSet,)
from .views import DynamicPygeoapiResourcesView
"""
from .viewsets import (ResourceViewSet, RasterLayerViewSet, DataTableViewSet, RemoteWMSViewSet,
                        PointVectorLayerViewSet, LineStringVectorLayerViewSet, PolygonVectorLayerViewSet,
                        MultiPointVectorLayerViewSet, MultiLineStringVectorLayerViewSet, MultiPolygonVectorLayerViewSet,
                       RemoteWFSViewSet)
"""

from base.router import drf_default_router

urlpatterns = [
    path('dynamic_pygeoapi_config/', DynamicPygeoapiResourcesView.as_view(), name='dynamic_pygeoapi_config'),
]

drf_default_router.register('rest/v1/resources/resources', ResourceViewSet, basename='resources-resources')
"""
drf_default_router.register('rest/v1/resources/point-vector-layers', PointVectorLayerViewSet, basename='resources-point-vector-layers')
drf_default_router.register('rest/v1/resources/linestring-vector-layers', LineStringVectorLayerViewSet, basename='resources-linestring-vector-layers')
drf_default_router.register('rest/v1/resources/polygon-vector-layers', PolygonVectorLayerViewSet, basename='resources-polygon-vector-layers')
drf_default_router.register('rest/v1/resources/multipoint-vector-layers', MultiPointVectorLayerViewSet, basename='resources-multipoint-vector-layers')
drf_default_router.register('rest/v1/resources/multilinestring-vector-layers', MultiLineStringVectorLayerViewSet, basename='resources-multilinestring-vector-layers')
drf_default_router.register('rest/v1/resources/multipolygon-vector-layers', MultiPolygonVectorLayerViewSet, basename='resources-multipolygon-vector-layers')
drf_default_router.register('rest/v1/resources/rasterlayers', RasterLayerViewSet, basename='resources-rasterlayers')
drf_default_router.register('rest/v1/resources/datatables', DataTableViewSet, basename='resources-datatables')
drf_default_router.register('rest/v1/resources/remotewms', RemoteWMSViewSet, basename='resources-remotewms')
drf_default_router.register('rest/v1/resources/remotewfs', RemoteWFSViewSet, basename='resources-remotewfs')
"""

if drf_default_router.urls not in urlpatterns:
    urlpatterns += drf_default_router.urls
