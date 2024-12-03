from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from .snippets import LayerFilesSnippetViewSetGroup
from .models import ResourcePointsFile
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.admin.viewsets import ViewSetGroup
#

register_snippet(LayerFilesSnippetViewSetGroup)
