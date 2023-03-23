from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='income-progression'),
    path('get-monthly-income-data/', views.get_monthly_income_data, name='get-monthly-income-data'),
]