from .models import PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer, \
    MultiLineStringVectorLayer, MultiPolygonVectorLayer
from wagtail.admin.panels import Panel, FieldPanel, InlinePanel, MultipleChooserPanel, MultiFieldPanel, FieldRowPanel, \
    TabbedInterface, ObjectList, AdminPageChooser, TitleFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from django_json_widget.widgets import JSONEditorWidget
from .widgets import CustomOSMWidget
from django.forms.formsets import DELETION_FIELD_NAME, ORDERING_FIELD_NAME
from django import forms
from wagtail.admin import compare
import functools
from taggit.forms import TagWidget

#


class FilesInlinePanel(InlinePanel):
    class BoundPanel(Panel.BoundPanel):
        template_name = "panels/files_inline_panel.html"

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.label = self.panel.label

            if self.form is None:
                return

            self.formset = self.form.formsets[self.panel.relation_name]
            self.child_edit_handler = self.panel.child_edit_handler

            self.children = []
            for index, subform in enumerate(self.formset.forms):
                # override the DELETE field to have a hidden input
                subform.fields[DELETION_FIELD_NAME].widget = forms.HiddenInput()

                # ditto for the ORDER field, if present
                if self.formset.can_order:
                    subform.fields[ORDERING_FIELD_NAME].widget = forms.HiddenInput()

                self.children.append(
                    self.child_edit_handler.get_bound_panel(
                        instance=subform.instance,
                        request=self.request,
                        form=subform,
                        prefix=("%s-%d" % (self.prefix, index)),
                    )
                )

            # if this formset is valid, it may have been re-ordered; respect that
            # in case the parent form errored, and we need to re-render
            if self.formset.can_order and self.formset.is_valid():
                self.children.sort(
                    key=lambda child: child.form.cleaned_data[ORDERING_FIELD_NAME] or 1
                )

            empty_form = self.formset.empty_form
            empty_form.fields[DELETION_FIELD_NAME].widget = forms.HiddenInput()
            if self.formset.can_order:
                empty_form.fields[ORDERING_FIELD_NAME].widget = forms.HiddenInput()

            self.empty_child = self.child_edit_handler.get_bound_panel(
                instance=empty_form.instance,
                request=self.request,
                form=empty_form,
                prefix=("%s-__prefix__" % self.prefix),
            )

        def get_comparison(self):
            field_comparisons = []

            for index, panel in enumerate(self.panel.child_edit_handler.children):
                field_comparisons.extend(
                    panel.get_bound_panel(
                        instance=None,
                        request=self.request,
                        form=None,
                        prefix=("%s-%d" % (self.prefix, index)),
                    ).get_comparison()
                )

            return [
                functools.partial(
                    compare.ChildRelationComparison,
                    self.panel.db_field,
                    field_comparisons,
                    label=self.label,
                )
            ]

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)
            context["can_order"] = self.formset.can_order
            return context


class FileFieldPanel(FieldPanel):
    def __init__(
            self,
            field_name,
            widget=None,
            disable_comments=None,
            permission=None,
            read_only=False,
            **kwargs,
    ):
        super().__init__(field_name, **kwargs)
        self.field_name = field_name
        self.widget = widget
        self.disable_comments = disable_comments
        self.permission = permission
        self.read_only = read_only


class VectorLayerSnippetViewSet(SnippetViewSet):
    add_to_admin_menu = False
    search_fields = ("title", "description", "category", "abstract", "purpose")
    list_filter = ("category", "topic_category", "license", "language", "date_type", "maintenance_frequency", "regions",
                   "restriction_code_type", "is_featured", "is_advertised")

    main_panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('category'),
        FieldPanel('tags'),
    ]

    metadata_panels = [
        FieldPanel('abstract'),
        FieldPanel('purpose'),
        FieldPanel('topic_category'),
        FieldPanel('date'),
        FieldPanel('date_type'),
        FieldPanel('edition'),
        FieldPanel('attribution'),
        FieldPanel('doi'),
        FieldPanel('maintenance_frequency'),
        FieldPanel('regions'),
        FieldPanel('restriction_code_type'),
        FieldPanel('other_constraints'),
        FieldPanel('license'),
        FieldPanel('language'),
        FieldPanel('spatial_representation_type'),
        FieldPanel('supplemental_information'),
        FieldPanel('data_quality_statement'),
    ]

    extra_panels = [
        FieldPanel('is_featured'),
        FieldPanel('is_advertised'),
        FieldPanel('thumbnail'),
    ]


class PointVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = PointVectorLayer
    menu_label = "Point Vector Layers"

    features_panels = [
        InlinePanel(
            relation_name='features',
            label="Features",
            classname="collapsed1",
            panels=[
                FieldPanel('id', heading=' '),
                FieldPanel('source_file', read_only=True),
                FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
                FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
            ]),
    ]

    files_panels = [
        FilesInlinePanel(
            relation_name='files',
            label="Files",
            classname="collapsed1",
            panels=[
                FieldPanel('collection', read_only=True),
                FieldPanel('title', read_only=True),
                FieldPanel('file', read_only=True),
            ]
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(features_panels, heading='Features'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Source Data Files'),
    ])


class LineStringVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = LineStringVectorLayer
    menu_label = "LineString Vector Layers"

    features_panels = [
        InlinePanel(
            relation_name='features',
            label="Features",
            classname="collapsed1",
            panels=[
                FieldPanel('id', heading=' '),
                FieldPanel('source_file', read_only=True),
                FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
                FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
            ]),
    ]

    files_panels = [
        FilesInlinePanel(
            relation_name='files',
            label="Files",
            classname="collapsed1",
            panels=[
                FieldPanel('collection', read_only=True),
                FieldPanel('title', read_only=True),
                FieldPanel('file', read_only=True),
            ]
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(features_panels, heading='Features'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Source Data Files'),
    ])


class PolygonVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = PolygonVectorLayer
    menu_label = "Polygon Vector Layers"

    features_panels = [
        InlinePanel(
            relation_name='features',
            label="Features",
            classname="collapsed1",
            panels=[
                FieldPanel('id', heading=' '),
                FieldPanel('source_file', read_only=True),
                FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
                FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
            ]),
    ]

    files_panels = [
        FilesInlinePanel(
            relation_name='files',
            label="Files",
            classname="collapsed1",
            panels=[
                FieldPanel('collection', read_only=True),
                FieldPanel('title', read_only=True),
                FieldPanel('file', read_only=True),
            ]
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(features_panels, heading='Features'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Source Data Files'),
    ])


class MultiPointVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = MultiPointVectorLayer
    menu_label = "MultiPoint Vector Layers"

    features_panels = [
        InlinePanel(
            relation_name='features',
            label="Features",
            classname="collapsed1",
            panels=[
                FieldPanel('id', heading=' '),
                FieldPanel('source_file', read_only=True),
                FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
                FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
            ]),
    ]

    files_panels = [
        FilesInlinePanel(
            relation_name='files',
            label="Files",
            classname="collapsed1",
            panels=[
                FieldPanel('collection', read_only=True),
                FieldPanel('title', read_only=True),
                FieldPanel('file', read_only=True),
            ]
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(features_panels, heading='Features'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Source Data Files'),
    ])


class MultiLineStringVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = MultiLineStringVectorLayer
    menu_label = "MultiLineString Vector Layers"

    features_panels = [
        InlinePanel(
            relation_name='features',
            label="Features",
            classname="collapsed1",
            panels=[
                FieldPanel('id', heading=' '),
                FieldPanel('source_file', read_only=True),
                FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
                FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
            ]),
    ]

    files_panels = [
        FilesInlinePanel(
            relation_name='files',
            label="Files",
            classname="collapsed1",
            panels=[
                FieldPanel('collection', read_only=True),
                FieldPanel('title', read_only=True),
                FieldPanel('file', read_only=True),
            ]
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(features_panels, heading='Features'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Source Data Files'),
    ])


class MultiPolygonVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = MultiPolygonVectorLayer
    menu_label = "MultiPolygon Vector Layers"

    features_panels = [
        InlinePanel(
            relation_name='features',
            label="Features",
            classname="collapsed1",
            panels=[
                FieldPanel('id', heading=' '),
                FieldPanel('source_file', read_only=True),
                FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
                FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
            ]),
    ]

    files_panels = [
        FilesInlinePanel(
            relation_name='files',
            label="Files",
            classname="collapsed1",
            panels=[
                FieldPanel('collection', read_only=True),
                FieldPanel('title', read_only=True),
                FieldPanel('file', read_only=True),
            ]
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(features_panels, heading='Features'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Source Data Files'),
    ])


class ResourcesSnippetViewSetGroup(SnippetViewSetGroup):
    items = [PointVectorLayerSnippetViewSet, LineStringVectorLayerSnippetViewSet, PolygonVectorLayerSnippetViewSet,
             MultiPointVectorLayerSnippetViewSet, MultiLineStringVectorLayerSnippetViewSet,
             MultiPolygonVectorLayerSnippetViewSet]
    menu_icon = "folder-open-inverse"
    menu_label = "Resources"
    menu_name = "resources"
