from django.db import models
from .mixins import ResourceBaseModelMixin

# Create your models here.


class ResourceCategory(ResourceBaseModelMixin):
    """
    Categories for resources.
    """

    class Meta:
        verbose_name = "Resource Category"
        verbose_name_plural = "Resource attributes: Resource Categories"
        ordering = ['title']
