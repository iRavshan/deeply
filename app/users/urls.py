from django.urls import path
from . import views

urlpatterns = [
    path('signIn', views.sign_in, name='signIn'),
    path('signUp', views.sign_up, name='signUp'),
    path('logout', views.log_out, name='logout'),
]