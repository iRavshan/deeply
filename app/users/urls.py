from django.urls import path
from . import views

urlpatterns = [
    path(r'signIn', views.sign_in, name='signIn'),
    path(r'signUp', views.sign_up, name='signUp'),
    path(r'logout', views.log_out, name='logout'),
]