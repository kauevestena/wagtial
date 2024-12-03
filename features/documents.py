from elasticsearch_dsl import Document, Text, Keyword, Date, GeoShape, Object

class PointFeatureDocument(Document):
    properties = Object()
    layer = Keyword()
    geom = GeoShape()
    last_published_at = Date()

    @classmethod
    def init(cls, index=None, using=None):
        cls._index.mapping = cls._doc_type.mapping
        cls._index.mapping.field('geom', 'geo_shape')
        cls._index.mapping.field('properties', 'object')
        super().init(index=index, using=using)

    class Index:
        name = 'pointvectorlayer'


class LineStringFeatureDocument(Document):
    data = Text()
    layer = Keyword()
    geom = GeoShape()
    last_published_at = Date()

    @classmethod
    def init(cls, index=None, using=None):
        cls._index.mapping = cls._doc_type.mapping
        cls._index.mapping.field('geom', 'geo_shape')
        super().init(index=index, using=using)

    class Index:
        name = 'linestringvectorlayer'


class PolygonFeatureDocument(Document):
    data = Text()
    layer = Keyword()
    geom = GeoShape()
    last_published_at = Date()

    @classmethod
    def init(cls, index=None, using=None):
        cls._index.mapping = cls._doc_type.mapping
        cls._index.mapping.field('geom', 'geo_shape')
        super().init(index=index, using=using)

    class Index:
        name = 'polygonvectorlayer'


PointFeatureDocument.init()
LineStringFeatureDocument.init()
PolygonFeatureDocument.init()
