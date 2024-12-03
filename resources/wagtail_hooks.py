from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from .snippets import (ResourcesSnippetViewSetGroup, )
#

register_snippet(ResourcesSnippetViewSetGroup)