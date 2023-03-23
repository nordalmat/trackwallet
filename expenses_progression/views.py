from authentication.models import User
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from expenses.models import Expense

from .utils import get_labels


def index(request):
    return render(request, 'progression/expenses.html')


@login_required(login_url='/authentication/login/')
def get_monthly_expense_data(request):
    current = timezone.now().date()
    current = current.replace(day=1)
    labels = get_labels(current)
    expenses_by_month = {}
    for key, value in labels.items():
        expenses = Expense.objects.filter(
            author=request.user, 
            expense_date__gte=current.replace(month=key), 
            expense_date__lt=current.replace(month=key)+relativedelta(months=1)
        )
        sum_expenses = expenses.aggregate(Sum('amount'))['amount__sum']
        if sum_expenses:
            expenses_by_month[value] = round(sum_expenses, 2)
        else:
            expenses_by_month[value] = 0
    user_currency = User.objects.filter(pk=request.user.id).first().currency.ticker
    return JsonResponse({'expenseData': expenses_by_month, 'userCurrency': user_currency}, safe=False)
