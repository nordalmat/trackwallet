from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='expenses-progression'),
    path('get-monthly-expense-data/', views.get_monthly_expense_data, name='get-monthly-expense-data'),
]