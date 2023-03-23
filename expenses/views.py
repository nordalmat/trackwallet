from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Category, Expense
from authentication.models import User


def index(request):
    if request.user.is_authenticated:
        today = timezone.now().date()
        past_expenses = Expense.objects.filter(author=request.user, expense_date__lte=today).order_by('-expense_date')
        planned_expenses = Expense.objects.filter(author=request.user, expense_date__gt=today).order_by('expense_date')
        return render(request, 'expenses/index.html', {
            'past_expenses': past_expenses,
            'planned_expenses': planned_expenses,
        })
    return render(request, 'expenses/index.html')


@login_required(login_url='/authentication/login/')
def add_expense(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', {
            'categories': categories
        })
    elif request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        category_id = request.POST.get('category', None)
        category = Category.objects.filter(pk=category_id).first()
        expense_date = request.POST['expense_date']
        today = timezone.now().date()
        if not expense_date:
            expense_date = str(today.strftime("%Y-%m-%d"))
        if not category:
            category = Category.objects.get(name='Else')
        if not amount:
            messages.error(request, 'Amount is required!')
            return render(request, 'expenses/add_expense.html', {
            'categories': categories,
            'request': request.POST,
            'selected_category': category
            })
        else:
            Expense.objects.create(
                author=request.user,
                amount=amount,
                description=description,
                category=category,
                expense_date=expense_date
            )
            messages.success(request, 'New expense added!')
            return redirect(reverse('expenses'))


@login_required(login_url='/authentication/login/')
def edit_expense(request, id):
    expense = Expense.objects.filter(pk=id).first()
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'expenses/edit_expense.html', {
            'expense': expense,
            'expense_id': expense.id,
            'categories': categories,
            'selected_category': expense.category
        })
    elif request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        category_id = request.POST.get('category', None)
        category = Category.objects.filter(pk=category_id).first()
        expense_date = request.POST['expense_date']
        today = timezone.now().date()
        if not expense_date:
            expense_date = str(today.strftime("%Y-%m-%d"))
        if not category:
            category = Category.objects.get(name='Else')
        if not amount:
            messages.error(request, 'Amount is required!')
            return render(request, 'expenses/edit_expense.html', {
                'categories': categories,
                'expense_id': expense.id,
                'expense': request.POST,
                'selected_category': category
            })
        else:
            expense.amount = amount
            expense.description = description
            expense.category = category
            expense.expense_date = expense_date
            expense.save()
            return redirect(reverse('expenses'))


@login_required(login_url='/authentication/login/')
def delete_expense(request, id):
    expense = Expense.objects.filter(pk=id).first()
    if expense is not None:
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
    else:
        messages.error(request, 'Expense was not found!')
    return redirect('expenses')
