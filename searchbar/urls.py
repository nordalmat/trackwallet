from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('search-expenses/', csrf_exempt(views.search_expenses), name='search-expenses'),
    path('search-category/', csrf_exempt(views.search_category), name='search-category'),
    path('search-currency/', csrf_exempt(views.search_currency), name='search-currency'),
    path('search-income/', csrf_exempt(views.search_income), name='search-income'),
    path('search-source/', csrf_exempt(views.search_source), name='search-source'),
]