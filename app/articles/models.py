import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from common.models import BaseModel
from users.models import CustomUser


class Article(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=200, null=False, blank=False)
    slug = models.SlugField(null=False, blank=True, editable=False)
    content = RichTextField(_('content'), null=False, blank=False)
    is_draft = models.BooleanField(default=True, null=False)
    views = models.PositiveIntegerField(default=0, null=False)
    upvotes = models.PositiveIntegerField(default=0, null=False)


    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)