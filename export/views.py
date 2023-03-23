import csv
import tempfile

import xlwt
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils import timezone
from expenses.models import Expense
from income.models import Income
from weasyprint import HTML


@login_required(login_url='/authentication/login/')
def export_csv_expenses(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + str(timezone.now().date()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Amount', 'Category', 'Description'])
    expenses = Expense.objects.filter(author=request.user).order_by('-expense_date')
    for expense in expenses:
        writer.writerow([expense.expense_date, expense.amount, expense.category.name, expense.description])
    return response


@login_required(login_url='/authentication/login/')
def export_xlsx_expenses(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + str(timezone.now().date()) + '.xlsx'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Date', 'Amount', 'Category', 'Description']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Expense.objects.filter(author=request.user).order_by('-expense_date').values_list('expense_date', 'amount', 'category', 'description')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


@login_required(login_url='/authentication/login/')
def export_pdf_expenses(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Expenses' + str(timezone.now().date()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    expenses = Expense.objects.filter(author=request.user).order_by('-expense_date')
    total = expenses.aggregate(Sum('amount'))
    html_string = render_to_string('export/pdf-output.html', {
        'expenses': expenses,
        'total': total,
    })
    html = HTML(string=html_string)
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


@login_required(login_url='/authentication/login/')
def export_csv_income(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Income' + str(timezone.now().date()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Amount', 'Source', 'Description'])
    income = Income.objects.filter(author=request.user).order_by('-income_date')
    for entry in income:
        writer.writerow([entry.income_date, entry.amount, entry.source.name, entry.description])
    return response


@login_required(login_url='/authentication/login/')
def export_xlsx_income(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Income' + str(timezone.now().date()) + '.xlsx'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Income')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Date', 'Amount', 'Source', 'Description']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Income.objects.filter(author=request.user).order_by('-income_date').values_list('income_date', 'amount', 'source', 'description')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


@login_required(login_url='/authentication/login/')
def export_pdf_income(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Income' + str(timezone.now().date()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    income = Income.objects.filter(author=request.user).order_by('-income_date')
    total = income.aggregate(Sum('amount'))
    html_string = render_to_string('export/pdf-output.html', {
        'income': income,
        'total': total,
    })
    html = HTML(string=html_string)
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


