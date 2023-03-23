from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Sum
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required

from authentication.models import User
from income.models import Income
from expenses_progression.utils import get_labels


def index(request):
    return render(request, 'progression/income.html')


@login_required(login_url='/authentication/login/')
def get_monthly_income_data(request):
    current = timezone.now().date()
    current = current.replace(day=1)
    labels = get_labels(current)
    income_by_month = {}
    for key, value in labels.items():
        incomes = Income.objects.filter(
            author=request.user, 
            income_date__gte=current.replace(month=key), 
            income_date__lt=current.replace(month=key)+relativedelta(months=1)
        )
        sum_incomes = incomes.aggregate(Sum('amount'))['amount__sum']
        if sum_incomes:
            income_by_month[value] = round(sum_incomes, 2)
        else:
            income_by_month[value] = 0
    user_currency = User.objects.filter(pk=request.user.id).first().currency.ticker
    return JsonResponse({'incomeData': income_by_month, 'userCurrency': user_currency}, safe=False)
