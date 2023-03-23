from authentication.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

from .models import Income, Source


def index(request):
    if request.user.is_authenticated:
        today = timezone.now().date()
        past_incomes = Income.objects.filter(author=request.user, income_date__lte=today).order_by('-income_date')
        planned_incomes = Income.objects.filter(author=request.user, income_date__gt=today).order_by('-income_date')
        return render(request, 'income/index.html', {
            'past_incomes': past_incomes,
            'planned_income': planned_incomes,
        })
    return render(request, 'income/index.html')


@login_required(login_url='/authentication/login/')
def add_income(request):
    sources = Source.objects.all()
    if request.method == 'GET':
        return render(request, 'income/add_income.html', {
            'sources': sources,
        })
    elif request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        source_id = request.POST.get('source')
        source = Source.objects.filter(pk=source_id).first()
        income_date = request.POST['income_date']
        today = timezone.now().date()
        if not income_date:
            income_date = str(today.strftime("%Y-%m-%d"))
        if not source:
            source = Source.objects.get(name='Else')
        if not amount:
            messages.error(request, 'Amount is required!')
            return render(request, 'income/add_income.html', {
                'sources': sources,
                'request': request.POST,
                'selected_source': source,
            })
        else:
            Income.objects.create(
                author=request.user,
                amount=amount,
                description=description,
                source=source,
                income_date=income_date
            )
            messages.success(request, 'New income added!')
            return redirect(reverse('income'))


@login_required(login_url='/authentication/login/')
def edit_income(request, id):
    income = Income.objects.filter(pk=id).first()
    sources = Source.objects.all()
    if request.method == 'GET':
        return render(request, 'income/edit_income.html', {
            'income': income,
            'income_id': income.id,
            'sources': sources,
            'selected_source': income.source
        })
    elif request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        source_id = request.POST.get('source', None)
        source = Source.objects.filter(pk=source_id).first()
        income_date = request.POST['income_date']
        today = timezone.now().date()
        if not income_date:
            income_date = str(today.strftime('%Y-%m-%d'))
        if not source:
            source = Source.objects.get(name='Else')
        if not amount:
            messages.error(request, 'Amount is required!')
            return render(request, 'income/edit_income.html', {
                'sources': sources,
                'income': request.POST,
                'income_id': income.id,
                'selected_source': source,
            })
        else:
            income.amount = amount
            income.description = description
            income.source = source
            income.income_date = income_date
            income.save()
            return redirect(reverse('income'))


@login_required(login_url='/authentication/login/')
def delete_income(request, id):
    income = Income.objects.filter(pk=id).first()
    if income is not None:
        income.delete()
        messages.success(request, 'Income deleted successfully!')
    else:
        messages.error(request, 'Income was not found!')
    return redirect('income')