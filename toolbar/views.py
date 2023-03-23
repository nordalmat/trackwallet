import json
from datetime import timedelta

from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from expenses.models import Expense
from income.models import Income


@login_required(login_url='/authentication/login/')
def expenses_days(request):
    if request.method == 'POST':
        num_days = json.loads(request.body)['days']
        today = timezone.now().date()
        expenses = Expense.objects.filter(author=request.user, expense_date__gt=today-timedelta(days=num_days), expense_date__lte=today).order_by('-expense_date')
        data = expenses.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/authentication/login/')
def income_days(request):
    if request.method == 'POST':
        num_days = json.loads(request.body)['days']
        today = timezone.now().date()
        income = Income.objects.filter(author=request.user, income_date__gt=today-timedelta(days=num_days), income_date__lte=today).order_by('-income_date')
        data = income.values()
        return JsonResponse(list(data), safe=False)
