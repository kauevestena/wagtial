from django.contrib.gis.db import models
from django.conf import settings
from wagtail.fields import RichTextField

GeoKnotTextField = RichTextField if settings.USE_RICHTEXT_TEXTFIELD else models.TextField
