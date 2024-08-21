from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Article, Tag

admin.site.register(Tag)
admin.site.register(Article, ImportExportModelAdmin)