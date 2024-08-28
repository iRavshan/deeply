from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models

admin.site.register(models.CourseLevel)
admin.site.register(models.CourseSubject)
admin.site.register(models.Course, ImportExportModelAdmin)
admin.site.register(models.Unit, ImportExportModelAdmin)
admin.site.register(models.Topic, ImportExportModelAdmin)
admin.site.register(models.CourseProgress, ImportExportModelAdmin)
admin.site.register(models.Glossary, ImportExportModelAdmin)