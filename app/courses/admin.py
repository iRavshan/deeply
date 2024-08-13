from django.contrib import admin
from . import models

admin.site.register(models.CourseLevel)
admin.site.register(models.CourseSubject)
admin.site.register(models.Course)
admin.site.register(models.Unit)
admin.site.register(models.Topic)
admin.site.register(models.CourseProgress)
