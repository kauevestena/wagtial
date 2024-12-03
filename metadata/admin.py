from django.contrib import admin
from .models import (ResourceMetadataDateType, ResourceMetadataLanguage, ResourceMetadataLicense,
                     ResourceMetadataMaintenanceFrequency, ResourceMetadataRegion, ResourceMetadataRestrictionCodeType,
                     ResourceMetadataSpatialRepresentationType, ResourceMetadataTopicCategory)

# Register your models here.

admin.site.register(ResourceMetadataDateType)
admin.site.register(ResourceMetadataLanguage)
admin.site.register(ResourceMetadataLicense)
admin.site.register(ResourceMetadataMaintenanceFrequency)
admin.site.register(ResourceMetadataRegion)
admin.site.register(ResourceMetadataRestrictionCodeType)
admin.site.register(ResourceMetadataSpatialRepresentationType)
admin.site.register(ResourceMetadataTopicCategory)
