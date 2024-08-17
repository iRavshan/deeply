from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:article_slug>', views.article, name='article'),
    path('tag/<slug:tag_slug>', views.tag, name='tag'),
]