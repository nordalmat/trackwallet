from django.urls import path

from . import views

urlpatterns = [
    path('', views.edit_preferences, name='preferences'),
]