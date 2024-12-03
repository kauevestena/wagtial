from wagtail.admin.forms.collections import CollectionChoiceField, SelectWithDisabledOptions
from wagtail.models import Collection
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.snippets.widgets import AdminSnippetChooser
from django import forms
from resources.models import PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer
from .models import ResourcePointsFile, ResourceLineStringsFile, ResourcePolygonsFile, ResourceMultiPointsFile, ResourceMultiLineStringsFile, ResourceMultiPolygonsFile

#


class EditResourceFileForm(WagtailAdminModelForm):
    collection = CollectionChoiceField(
        queryset=Collection.objects.all(),
        widget=SelectWithDisabledOptions,
    )

    class Meta:
        model = ResourcePointsFile
        fields = ['collection', 'title']


class NewResourceFileFormMixin(WagtailAdminModelForm):
    collection = CollectionChoiceField(
        queryset=Collection.objects.all(),
        widget=SelectWithDisabledOptions,
    )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.uploaded_by_user:
            instance.uploaded_by_user = self.for_user
        if commit:
            instance.save()
        return instance


class NewResourcePointsFileForm(NewResourceFileFormMixin):
    layer = forms.ModelChoiceField(
        queryset=PointVectorLayer.objects.all(),
        widget=AdminSnippetChooser(PointVectorLayer)
    )

    class Meta:
        model = ResourcePointsFile
        fields = ['collection', 'title', 'file', 'layer']


class NewResourceLineStringsFileForm(NewResourceFileFormMixin):
    layer = forms.ModelChoiceField(
        queryset=LineStringVectorLayer.objects.all(),
        widget=AdminSnippetChooser(LineStringVectorLayer)
    )

    class Meta:
        model = ResourceLineStringsFile
        fields = ['collection', 'title', 'file', 'layer']


class NewResourcePolygonsFileForm(NewResourceFileFormMixin):
    layer = forms.ModelChoiceField(
        queryset=PolygonVectorLayer.objects.all(),
        widget=AdminSnippetChooser(PolygonVectorLayer)
    )

    class Meta:
        model = ResourcePolygonsFile
        fields = ['collection', 'title', 'file', 'layer']


class NewResourceMultiPointsFileForm(NewResourceFileFormMixin):
    layer = forms.ModelChoiceField(
        queryset=MultiPointVectorLayer.objects.all(),
        widget=AdminSnippetChooser(MultiPointVectorLayer)
    )

    class Meta:
        model = ResourceMultiPointsFile
        fields = ['collection', 'title', 'file', 'layer']


class NewResourceMultiLineStringsFileForm(NewResourceFileFormMixin):
    layer = forms.ModelChoiceField(
        queryset=MultiLineStringVectorLayer.objects.all(),
        widget=AdminSnippetChooser(MultiLineStringVectorLayer)
    )

    class Meta:
        model = ResourceMultiLineStringsFile
        fields = ['collection', 'title', 'file', 'layer']


class NewResourceMultiPolygonsFileForm(NewResourceFileFormMixin):
    layer = forms.ModelChoiceField(
        queryset=MultiPolygonVectorLayer.objects.all(),
        widget=AdminSnippetChooser(MultiPolygonVectorLayer)
    )

    class Meta:
        model = ResourceMultiPolygonsFile
        fields = ['collection', 'title', 'file', 'layer']
