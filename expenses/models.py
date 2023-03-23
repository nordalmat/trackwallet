import datetime
import json

from authentication.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    class Meta:
        verbose_name_plural = 'Categories'


class Expense(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expenses')
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories_expenses')
    description = models.CharField(max_length=150, null=True, blank=True)
    expense_date = models.DateField(default=datetime.date.today, null=True, blank=True)

    def __str__(self):
        return f"{self.author} -> {self.amount} ({self.category})"
    
