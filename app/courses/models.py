from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from common.models import BaseModel
from users.models import CustomUser


class CourseSubject(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, unique=True)

    def __str__(self) -> str:
        return self.name


class CourseLevel(models.Model):
    name = models.CharField(_('name'), max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Glossary(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, auto_created=True, editable=False)
    subject = models.ForeignKey(CourseSubject, on_delete=models.CASCADE)
    term = models.CharField(_('term'), max_length=70, null=False, blank=False)
    definition = RichTextField(_('definition'), null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.subject.name}: {self.term} - {self.definition}'
    
    class Meta:
        unique_together = ('subject', 'term')
        ordering = ['term']
        verbose_name_plural = 'Glossaries'


class Course(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    title = models.CharField(_('title'), max_length=250, null=False)
    slug = models.SlugField(_('slug'), unique=True, null=False, blank=True)
    instructor = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    level = models.ForeignKey(CourseLevel, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(CourseSubject, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Unit(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    title = models.CharField(_('title'), max_length=250, null=False)
    slug = models.SlugField(_('slug'), null=False, blank=True)
    course = models.ForeignKey(Course, null=False, blank=True, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(null=False, blank=True, editable=False)

    class Meta:
        unique_together = ('course', 'slug')
        ordering = ['order']
        
    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.order is None:
            self.set_order()
        super().save(*args, **kwargs)
    
    def set_order(self):
        max_order = Unit.objects.filter(course=self.course).aggregate(models.Max('order'))['order__max']
        self.order = 0 if max_order is None else max_order + 1
    

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.reorder_units()


    def reorder_units(self):
        units = Unit.objects.filter(course=self.course).order_by('order')
        for index, unit in enumerate(units):
            unit.order = index
            unit.save(update_fields=['order'])
    


class Topic(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    title = models.CharField(_('title'), max_length=300, null=False)
    slug = models.SlugField(_('slug'), null=False, blank=True)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.SET_NULL)
    content = RichTextField(_('content'), null=False)
    order = models.PositiveSmallIntegerField(null=False, blank=True, editable=False)
    github_url = models.URLField(null=True, blank=True)
    notebook_url = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ('course', 'unit', 'slug')
        ordering = ['order']

    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.order is None:
            self.set_order()
        super().save(*args, **kwargs)
    

    def set_order(self):
        max_order = Topic.objects.filter(course=self.course).aggregate(models.Max('order'))['order__max']
        self.order = 0 if max_order is None else max_order + 1
    

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.reorder_topics()


    def reorder_topics(self):
        topics = Topic.objects.filter(course=self.course).order_by('order')
        for index, topic in enumerate(topics):
            topic.order = index
            topic.save(update_fields=['order'])


class CourseProgress(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    last_completed_topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL, blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.email} - {self.course.title}'
    
    class Meta:
        verbose_name_plural = _('Course progresses')