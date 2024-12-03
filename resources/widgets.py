from django.contrib.gis import forms as gis_forms


class CustomOSMWidget(gis_forms.OSMWidget):
    default_lat = 27.5  # Latitud predeterminada
    default_lon = -100.1  # Longitud predeterminada
    default_zoom = 4   # Nivel de zoom predeterminado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_srid = 3857

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['default_lat'] = self.default_lat
        context['default_lon'] = self.default_lon
        context['default_zoom'] = self.default_zoom
        return context
