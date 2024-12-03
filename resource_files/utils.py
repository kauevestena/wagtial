import fiona
from fiona.transform import transform_geom
from django.core.exceptions import ValidationError
import os
from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry
import json
from shapely.geometry import shape


# TODO: Create a function that will take a file and readit using fiona to get the crs and convert the data to data able to store in geom field on geodjango
# TODO: create a function to store data in a geodjango model


def get_spatial_data_features(file):
    try:
        file_ext = file.split('.').pop()
        if file_ext in ['zip']:
            with open(file, 'rb') as disk_file:
                with fiona.io.ZipMemoryFile(disk_file) as mem_file:
                    layers = mem_file.listlayers()
                    layer = mem_file.open(layer=layers.pop())
                    for feature in layer:
                        yield feature, layer.crs
        elif file_ext in ['gpkg', 'geojson']:
            with fiona.open(file) as layer:
                for feature in layer:
                    yield feature, layer.crs
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def store_layer_data(file, layer, model):
    try:
        print("store_layer_data file", file)
        print("store_layer_data layer", layer)
        print("store_layer_data model", model)

        if not model.objects.filter(layer=layer, source_file=file).exists():
            for feature, crs in get_spatial_data_features(file.file.path):
                properties = dict(feature['properties'])
                reprojected_geometry = transform_geom(crs, settings.DATA_FEATURES_SRID, feature['geometry'])
                shapely_geometry = shape(reprojected_geometry)
                if layer and file.id and shapely_geometry and properties:
                    new_feature = model(layer=layer, source_file=file, geom=shapely_geometry.wkt, data=properties)
                    new_feature.save()
                    print("new_feature", new_feature)
                else:
                    print("Error", shapely_geometry)

    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def uuid_file_path(instance, filename):
    """
    Returns the file path for the FileField upload_to parameter,
    using the UUID of the instance as the filename.
    """
    ext = filename.split('.').pop()
    if not ext:
        raise ValidationError("El archivo debe tener extensión")
    file_name = filename.replace(' ', '_')
    filename = f"{instance.layer.pk}--{file_name}"
    file_path = os.path.join('resource_data_files/', filename)
    return file_path


def validate_point_vector_file(file):
    print("validate_point_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['Point']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['Point']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def validate_linestring_vector_file(file):
    print("validate_point_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['LineString']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['LineString']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def validate_polygon_vector_file(file):
    print("validate_point_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['Polygon']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['Polygon']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def validate_multipoint_vector_file(file):
    print("validate_multipoint_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['MultiPoint']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['MultiPoint']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def validate_multilinestring_vector_file(file):
    print("validate_multipoint_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['MultiLineString']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['MultiLineString']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def validate_multipolygon_vector_file(file):
    print("validate_multipolygon_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['MultiPolygon']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['MultiPolygon']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)
