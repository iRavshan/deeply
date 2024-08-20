from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from common.models import BaseModel
from users.models import CustomUser


class Tag(BaseModel):
    name = models.CharField(unique=True, null=False, max_length=30)
    slug = models.SlugField(null=False, blank=True, editable=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    author = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=200, null=False, blank=False)
    slug = models.SlugField(null=False, blank=True, editable=False)
    content = RichTextField(_('content'), null=False, blank=False)
    description = models.TextField(_('description'), null=True)
    tags = models.ManyToManyField(Tag)
    is_draft = models.BooleanField(default=True, null=False)
    views = models.PositiveIntegerField(default=0, null=False)
    upvotes = models.PositiveIntegerField(default=0, null=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.title} by {self.author.email}'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'