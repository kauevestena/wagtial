from .models import (ResourcePointsFile, ResourceLineStringsFile, ResourcePolygonsFile, ResourceMultiPointsFile, ResourceMultiLineStringsFile, ResourceMultiPolygonsFile)
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from .forms import (EditResourceFileForm, NewResourcePointsFileForm, NewResourceLineStringsFileForm,
                    NewResourcePolygonsFileForm, NewResourceMultiPointsFileForm,
                    NewResourceMultiLineStringsFileForm, NewResourceMultiPolygonsFileForm)

#


class ResourcePointsFileSnippetViewSet(SnippetViewSet):
    model = ResourcePointsFile
    menu_label = "Point Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer")
    list_filter = ("layer", "collection", "uploaded_by_user")
    list_display = ("title", "layer", "collection", "uploaded_by_user", "created_at")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourceFileForm
        return NewResourcePointsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class ResourceLineStringsFileSnippetViewSet(SnippetViewSet):
    model = ResourceLineStringsFile
    menu_label = "LineString Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer")
    list_filter = ("layer", "collection", "uploaded_by_user")
    list_display = ("title", "layer", "collection", "uploaded_by_user", "created_at")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourceFileForm
        return NewResourceLineStringsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class ResourcePolygonsFileSnippetViewSet(SnippetViewSet):
    model = ResourcePolygonsFile
    menu_label = "Polygon Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer")
    list_filter = ("layer", "collection", "uploaded_by_user")
    list_display = ("title", "layer", "collection", "uploaded_by_user", "created_at")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourceFileForm
        return NewResourcePolygonsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class ResourceMultiPointsFileSnippetViewSet(SnippetViewSet):
    model = ResourceMultiPointsFile
    menu_label = "MultiPoint Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer")
    list_filter = ("layer", "collection", "uploaded_by_user")
    list_display = ("title", "layer", "collection", "uploaded_by_user", "created_at")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourceFileForm
        return NewResourceMultiPointsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class ResourceMultiLineStringsFileSnippetViewSet(SnippetViewSet):
    model = ResourceMultiLineStringsFile
    menu_label = "MultiLineString Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer")
    list_filter = ("layer", "collection", "uploaded_by_user")
    list_display = ("title", "layer", "collection", "uploaded_by_user", "created_at")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourceFileForm
        return NewResourceMultiLineStringsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class ResourceMultiPolygonsFileSnippetViewSet(SnippetViewSet):
    model = ResourceMultiPolygonsFile
    menu_label = "MultiPolygon Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer")
    list_filter = ("layer", "collection", "uploaded_by_user")
    list_display = ("title", "layer", "collection", "uploaded_by_user", "created_at")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourceFileForm
        return NewResourceMultiPolygonsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class LayerFilesSnippetViewSetGroup(SnippetViewSetGroup):
    items = [ResourcePointsFileSnippetViewSet, ResourceLineStringsFileSnippetViewSet,
             ResourcePolygonsFileSnippetViewSet, ResourceMultiPointsFileSnippetViewSet,
             ResourceMultiLineStringsFileSnippetViewSet, ResourceMultiPolygonsFileSnippetViewSet]
    menu_icon = "folder-open-inverse"
    menu_label = "Source Data Files"
    menu_name = "data-files"
