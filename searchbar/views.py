import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from expenses.models import Category, Expense
from income.models import Income, Source
from preferences.models import Currency


@login_required(login_url='/authentication/login/')
def search_expenses(request):
    if request.method == 'POST':
        search_value = json.loads(request.body).get('searchValue')
        expenses = Expense.objects.filter(
            Q(amount__startswith=search_value) |
            Q(category__name__icontains=search_value) |
            Q(description__icontains=search_value) |
            Q(expense_date__icontains=search_value),
            author=request.user
        ).order_by('-expense_date')
        data = expenses.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/authentication/login/')
def search_category(request):
    if request.method == 'POST':
        category_id = json.loads(request.body).get('category_id')
        category = Category.objects.filter(id=category_id).first()
        return JsonResponse(category.to_json(), safe=False)


@login_required(login_url='/authentication/login/')
def search_currency(request):
    if request.method == 'POST':
        user_id = json.loads(request.body).get('user_id')
        currency = User.objects.filter(pk=user_id).currency.name
        if currency:
            return JsonResponse(category, safe=False)
        return None


@login_required(login_url='/authentication/login/')
def search_income(request):
    if request.method == 'POST':
        search_value = json.loads(request.body).get('searchValue')
        incomes = Income.objects.filter(
            Q(amount__startswith=search_value) |
            Q(source__name__icontains=search_value) |
            Q(description__icontains=search_value) |
            Q(income_date__icontains=search_value),
            author=request.user
        ).order_by('-income_date')
        data = incomes.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/authentication/login/')
def search_source(request):
    if request.method == 'POST':
        source_id = json.loads(request.body).get('source_id')
        source = Source.objects.filter(pk=source_id).first()
        return JsonResponse(source.to_json(), safe=False)


        

