from django.contrib import admin
from url_shortener.models import LinkModel


@admin.register(LinkModel)
class LinkModelAdmin(admin.ModelAdmin):
    list_display = ("link_key", "get_link")

    @admin.display(description='link')
    def get_link(self, object):
        return object.link[:30] + "..."
