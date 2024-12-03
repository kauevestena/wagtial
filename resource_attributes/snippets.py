from wagtail.snippets.models import register_snippet
from .models import ResourceCategory
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import PageChooserPanel

@register_snippet
class ResourceCategorySnippetViewSet(SnippetViewSet):
    model = ResourceCategory
    menu_label = "Resource Attribute: Categories"
    add_to_admin_menu = False
    search_fields = ("title",)

    panels = [
        FieldPanel('title'),
    ]

