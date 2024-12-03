from .viewsets import (PointViewSet, )

# from .viewsets import (PointViewSet, LineStringViewSet, PolygonViewSet, MultiPointViewSet, MultiLineStringViewSet, MultiPolygonViewSet, GeometryCollectionViewSet)
from .viewsets import (PointGeoFeatureViewSet, )
# from .viewsets import (PointGeoFeatureViewSet, LineStringGeoFeatureViewSet, PolygonGeoFeatureViewSet, MultiPointGeoFeatureViewSet, MultiLineStringGeoFeatureViewSet, MultiPolygonGeoFeatureViewSet, GeometryCollectionGeoFeatureViewSet)
from base.router import drf_default_router

urlpatterns = []

drf_default_router.register('rest/v1/features/points', PointViewSet, basename='points')
"""
drf_default_router.register('rest/v1/features/linestrings', LineStringViewSet, basename='linestrings')
drf_default_router.register('rest/v1/features/polygons', PolygonViewSet, basename='polygons')
drf_default_router.register('rest/v1/features/multipoints', MultiPointViewSet, basename='multipoints')
drf_default_router.register('rest/v1/features/multilinestrings', MultiLineStringViewSet, basename='multilinestrings')
drf_default_router.register('rest/v1/features/multipolygons', MultiPolygonViewSet, basename='multipolygons')
drf_default_router.register('rest/v1/features/geometrycollections', GeometryCollectionViewSet, basename='geometrycollections')
"""

drf_default_router.register('rest/v1/features/geojson/points', PointGeoFeatureViewSet, basename='geojson-points')
"""
drf_default_router.register('rest/v1/features/geojson/linestrings', LineStringGeoFeatureViewSet, basename='geojson-linestrings')
drf_default_router.register('rest/v1/features/geojson/polygons', PolygonGeoFeatureViewSet, basename='geojson-polygons')
drf_default_router.register('rest/v1/features/geojson/multipoints', MultiPointGeoFeatureViewSet, basename='geojson-multipoints')
drf_default_router.register('rest/v1/features/geojson/multilinestrings', MultiLineStringGeoFeatureViewSet, basename='geojson-multilinestrings')
drf_default_router.register('rest/v1/features/geojson/multipolygons', MultiPolygonGeoFeatureViewSet, basename='geojson-multipolygons')
drf_default_router.register('rest/v1/features/geojson/geometrycollections', GeometryCollectionGeoFeatureViewSet, basename='geojson-geometrycollections')
"""

if drf_default_router.urls not in urlpatterns:
    urlpatterns += drf_default_router.urls