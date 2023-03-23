from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('expenses-days/', csrf_exempt(views.expenses_days), name='expenses-days'),
    path('income-days/', csrf_exempt(views.income_days), name='income-days'),
]