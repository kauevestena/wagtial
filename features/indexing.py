from elasticsearch_dsl.connections import connections
from .models import Point, LineString, Polygon
from .documents import PointFeatureDocument, LineStringFeatureDocument, PolygonFeatureDocument

connections.create_connection()

def index_point_features():
    for feature in Point.objects.all():
        doc = PointFeatureDocument(
            meta={'id': feature.id},
            title=feature.title,
            description=feature.description,
            resource_layer_id=feature.resource_layer.id,
            tags=[tag.name for tag in feature.tags.all()],
            geom=feature.geom.geojson,
            last_published_at=feature.last_published_at
        )
        doc.save()

def index_linestring_features():
    for feature in LineString.objects.all():
        doc = LineStringFeatureDocument(
            meta={'id': feature.id},
            title=feature.title,
            description=feature.description,
            resource_layer_id=feature.resource_layer.id,
            tags=[tag.name for tag in feature.tags.all()],
            geom=feature.geom.geojson,
            last_published_at=feature.last_published_at
        )
        doc.save()

def index_polygon_features():
    for feature in Polygon.objects.all():
        doc = PolygonFeatureDocument(
            meta={'id': feature.id},
            title=feature.title,
            description=feature.description,
            resource_layer_id=feature.resource_layer.id,
            tags=[tag.name for tag in feature.tags.all()],
            geom=feature.geom.geojson,
            last_published_at=feature.last_published_at
        )
        doc.save()

index_point_features()
index_linestring_features()
index_polygon_features()
