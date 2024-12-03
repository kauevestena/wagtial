import logging
import json
from pygeoapi.provider.base import BaseProvider, ProviderItemNotFoundError
from features.models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from features.serializers import (
    PointGeoFeatureSerializer, LineStringGeoFeatureSerializer, PolygonGeoFeatureSerializer,
    MultiPointGeoFeatureSerializer, MultiLineStringGeoFeatureSerializer, MultiPolygonGeoFeatureSerializer
)
from resources.models import (
    Resource, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer,
    MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer
)
from django.contrib.gis.db.models import Extent
from django.db.models import Min, Max
import httpx
LOGGER = logging.getLogger(__name__)


class TilingScheme:
    def __init__(self, tileMatrixSetURI, crs, tileMatrixSet):
        self.tileMatrixSetURI = tileMatrixSetURI
        self.crs = crs
        self.tileMatrixSet = tileMatrixSet


class WagtailProvider(BaseProvider):
    def __init__(self, provider_def):
        super().__init__(provider_def)
        self.layer_id = provider_def.get('data')
        self.tile_type = provider_def.get('tile_type', 'vector')
        self.format_type = provider_def.get('format_type', 'GeoJSON')
        self.model_map = {
            PointVectorLayer: (Point, PointGeoFeatureSerializer),
            LineStringVectorLayer: (LineString, LineStringGeoFeatureSerializer),
            PolygonVectorLayer: (Polygon, PolygonGeoFeatureSerializer),
            MultiPointVectorLayer: (MultiPoint, MultiPointGeoFeatureSerializer),
            MultiLineStringVectorLayer: (MultiLineString, MultiLineStringGeoFeatureSerializer),
            MultiPolygonVectorLayer: (MultiPolygon, MultiPolygonGeoFeatureSerializer)
        }

    def _get_queryset_and_serializer(self):
        resource_layer = Resource.objects.get(id=self.layer_id)
        real_instance = resource_layer.get_real_instance()
        model_class, serializer_class = self.model_map.get(type(real_instance), (None, None))
        if model_class is None:
            raise ValueError('Invalid layer type')
        return model_class.objects.filter(layer_id=self.layer_id), serializer_class

    def query(self, offset=0, limit=10, resulttype='results', bbox=None, datetime_=None, properties=None, sortby=None,
              select_properties=None, skip_geometry=False, q=None, **kwargs):
        if select_properties is None:
            select_properties = []
        if sortby is None:
            sortby = []
        if properties is None:
            properties = []
        if bbox is None:
            bbox = []
        queryset, serializer_class = self._get_queryset_and_serializer()
        total_count = queryset.count()
        queryset = queryset[offset:offset + limit]
        serializer = serializer_class(queryset, many=True)

        serializer.data['numberMatched'] = total_count
        serializer.data['numberReturned'] = len(serializer.data['features'])

        json_data = json.dumps(serializer.data)
        print("json_data", json_data)
        return json.loads(json_data)

    def get(self, identifier, **kwargs):
        queryset, serializer_class = self._get_queryset_and_serializer()
        try:
            instance = queryset.get(id=identifier)
            serializer = serializer_class(instance)
            return serializer.data
        except queryset.model.DoesNotExist:
            raise ProviderItemNotFoundError(f'Item {identifier} not found')

    def create(self, new_feature):
        _, serializer_class = self._get_queryset_and_serializer()
        serializer = serializer_class(data=new_feature)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValueError('Invalid data')

    def update(self, identifier, new_feature):
        queryset, serializer_class = self._get_queryset_and_serializer()
        try:
            instance = queryset.get(id=identifier)
            serializer = serializer_class(instance, data=new_feature)
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValueError('Invalid data')
        except queryset.model.DoesNotExist:
            raise ProviderItemNotFoundError(f'Item {identifier} not found')

    def delete(self, identifier):
        queryset, serializer_class = self._get_queryset_and_serializer()
        try:
            instance = queryset.get(id=identifier)
            instance.delete()
        except queryset.model.DoesNotExist:
            raise ProviderItemNotFoundError(f'Item {identifier} not found')

    def get_layer(self):
        try:
            resource_layer = Resource.objects.get(id=self.layer_id)
            real_instance = resource_layer.get_real_instance()
            features = real_instance.features.all()
            return features
        except Resource.DoesNotExist:
            raise ProviderItemNotFoundError(f'Layer with id {self.layer_id} not found')



    """
    
    def get_metadata(self, dataset, server_url, layer, tileset, metadata_format, title, description, language):
        try:
            resource_layer = Resource.objects.get(id=self.layer_id)
            real_instance = resource_layer.get_real_instance()
            metadata = {
                "title": title,
                "description": description,
                "keywords": list(real_instance.tags.all().values_list('name', flat=True)),
                "extents": {
                    "spatial": {
                        "bbox": real_instance.features.aggregate(Extent('geom'))['geom__extent'],
                        'crs': 'http://www.opengis.net/def/crs/OGC/1.3/CRS84'
                    },
                    "temporal": {
                        "begin": real_instance.features.aggregate(begin=Min('last_published_at'))['begin'],
                        "end": real_instance.features.aggregate(end=Max('last_published_at'))['end']
                    }
                },
                "server_url": server_url,
                "dataset": dataset,
                "layer": layer,
                "tileset": tileset,
                "metadata_format": metadata_format,
                "language": language
            }
            return metadata
        except Resource.DoesNotExist:
            raise ProviderItemNotFoundError(f'Layer with id {self.layer_id} not found')

    def get_data_tiles(self, z, x, y):
        url = f"https://8408c9deeb14462e9828caee0f63a531.us-central1.gcp.cloud.es.io/{self.polymorphic_ctype.model}/_mvt/geom/{z}/{x}/{y}"
        response = httpx.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ProviderItemNotFoundError(f"Tile data not found for {z}/{x}/{y}")

    def get_tiles_service(self, baseurl, servicepath):
        return {
            "type": "vector",
            "tiles": [
                f"{baseurl}/collections/{self.layer_id}/tiles/{{z}}/{{x}}/{{y}}"
            ],
            "links": [
                {
                    "href": f"{baseurl}/collections/{self.layer_id}/tiles",
                    "rel": "self",
                    "type": "application/json",
                    "title": "Tiles"
                }
            ]
        }

    def get_tiling_schemes(self):
        return [
            TilingScheme(
                tileMatrixSetURI='https://www.opengis.net/def/tilematrixset/OGC/1.0/WebMercatorQuad',
                crs='EPSG:3857',
                tileMatrixSet='WebMercatorQuad'
            ),
            TilingScheme(
                tileMatrixSetURI='https://www.opengis.net/def/tilematrixset/OGC/1.0/WebMercator',
                crs='EPSG:3857',
                tileMatrixSet='WebMercator'
            ),
            
        ]
    """

    def __repr__(self):
        return f'<WagtailProvider> layer_id={self.layer_id}'
