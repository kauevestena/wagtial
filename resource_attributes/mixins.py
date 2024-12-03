from django.db import models
from base.mixins import LockableRevisionModelBaseAbstract
from autoslug import AutoSlugField

# Create your mixins here.


class ResourceBaseModelMixin(LockableRevisionModelBaseAbstract):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
