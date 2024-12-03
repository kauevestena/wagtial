from django.shortcuts import render
from elasticsearch_dsl import Search
from django.http import JsonResponse
from .documents import PointFeatureDocument, LineStringFeatureDocument, PolygonFeatureDocument


# Create your views here.

def search_features(request):
    layer = request.GET.get('layer')
    point_search = Search(index='pointvectorlayer').filter('term', layer=layer)
    linestring_search = Search(index='linestringvectorlayer').filter('term', layer=layer)
    polygon_search = Search(index='polygonvectorlayer').filter('term', layer=layer)

    point_response = point_search.execute()
    linestring_response = linestring_search.execute()
    polygon_response = polygon_search.execute()

    results = {
        'point_features': [hit.to_dict() for hit in point_response],
        'linestring_features': [hit.to_dict() for hit in linestring_response],
        'polygon_features': [hit.to_dict() for hit in polygon_response]
    }

    return JsonResponse(results, safe=False)
