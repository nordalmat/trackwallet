import json

from authentication.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from preferences.models import Currency


def edit_preferences(request):
    if request.user.is_authenticated:
        user = User.objects.filter(id=request.user.id).first()
        user_currency = user.currency
        currency_data = Currency.objects.all()
        if request.method == 'GET':
            return render(request, 'preferences/preferences.html', {
                'currency_data': currency_data,
                'user_currency': user_currency,
            })
        elif request.method == 'POST':
            select = request.POST['currency']
            currency = Currency.objects.filter(ticker=select).first()
            user.currency = currency
            user.save()
            messages.success(request, 'Preferences saved successfully!')
            return redirect(reverse('preferences'))
    return render(request, 'preferences/preferences.html')