# middleware.py
from os import getenv

import httpx
from django.conf import settings
from pygeoapi.util import yaml_load


class DynamicPygeoapiConfigMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/ogcapi/'):
            print('Request path starts with /ogcapi/')
            base_url = request.build_absolute_uri('/')
            config_url = f'{base_url}dynamic_pygeoapi_config/'
            print(f'Fetching dynamic config from {config_url}')
            response = httpx.get(config_url)
            print(f'Response: {response}')

            if response.status_code == 200:
                dynamic_config = response.json()
                # Cargar la configuración original desde config.yml
                with open(getenv('PYGEOAPI_CONFIG', 'pygeoapi.config.yml'), 'r') as f:
                    original_config = yaml_load(f)
                # Actualizar solo la sección de resources
                original_config['resources'] = dynamic_config.get('resources', {})
                print("resources config", original_config)
                settings.PYGEOAPI_CONFIG = original_config
        response = self.get_response(request)
        return response
