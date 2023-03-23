from django.urls import path

from . import views

urlpatterns = [
    path('export-csv-expenses/', views.export_csv_expenses, name='export-csv-expenses'),
    path('export-xlsx-expenses/', views.export_xlsx_expenses, name='export-xlsx-expenses'),
    path('export-pdf-expenses/', views.export_pdf_expenses, name='export-pdf-expenses'),
    path('export-csv-income/', views.export_csv_income, name='export-csv-income'),
    path('export-xlsx-income/', views.export_xlsx_income, name='export-xlsx-income'),
    path('export-pdf-income/', views.export_pdf_income, name='export-pdf-income'),
]
