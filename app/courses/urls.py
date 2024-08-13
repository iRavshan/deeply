from django.urls import path
from . import views

urlpatterns = [
    path('<slug:course_slug>/', views.course, name='course'),
    path('<slug:course_slug>/<slug:topic_slug>', views.topic, name='topic'),
]