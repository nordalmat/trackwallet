from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Sum
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required

from .utils import expense_summary, income_summary
from authentication.models import User
from expenses.models import Expense, Category
from income.models import Income, Source
from preferences.models import Currency


def index(request):
    if request.user.is_authenticated:
        current = timezone.now().date()
        current = current.replace(day=1)
        user = User.objects.filter(username=request.user).first()
        currency = None
        if user.currency:
            currency = user.currency.ticker
        expenses = Expense.objects.filter(author=request.user, expense_date__gte=current, expense_date__lt=current+relativedelta(months=1))
        total_expenses = expenses.aggregate(Sum('amount'))
        income = Income.objects.filter(author=request.user, income_date__gte=current, income_date__lt=current+relativedelta(months=1))
        total_income = income.aggregate(Sum('amount'))
        net = total_income['amount__sum'] - total_expenses['amount__sum']
        expense_data = expense_summary(expenses)
        top_category = max(expense_data, key=expense_data.get)
        return render(request, 'dashboard/index.html', {
            'current_month': current.strftime('%B'),
            'currency': currency,
            'total_expenses': round(total_expenses['amount__sum'], 2),
            'total_income': round(total_income['amount__sum'], 2),
            'net': round(net, 2),
            'top_category': top_category,
        })
    return render(request, 'dashboard/index.html')


@login_required(login_url='/authentication/login/')
def get_expenses_data(request):
    current = timezone.now().date()
    current = current.replace(day=1)
    expenses = Expense.objects.filter(author=request.user, expense_date__gte=current, expense_date__lt=current+relativedelta(months=1))
    expense_data = expense_summary(expenses)
    return JsonResponse({'expenseData': expense_data}, safe=False)


@login_required(login_url='/authentication/login/')
def get_income_data(request):
    current = timezone.now().date()
    current = current.replace(day=1)
    incomes = Income.objects.filter(author=request.user, income_date__gte=current, income_date__lt=current+relativedelta(months=1))
    income_data = income_summary(incomes)
    return JsonResponse({'incomeData': income_data}, safe=False)