from django.contrib import admin
from .models import Post, Tag
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
class EntryAdmin(MarkdownModelAdmin):
	list_display = ('title', 'create_date')
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, EntryAdmin)
admin.site.register(Tag)