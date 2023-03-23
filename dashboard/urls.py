from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('get-expenses-data/', views.get_expenses_data, name='get-expenses-data'),
    path('get-income-data/', views.get_income_data, name='get-income-data'),
]