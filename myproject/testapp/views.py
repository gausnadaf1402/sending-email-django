from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from . import forms

def Subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        if sub.is_valid():
            subject = 'Welcome to sendEmailUsingDjango'
            message = 'Hope you are enjoying this'
            email_from = settings.EMAIL_HOST_USER
            recepient = sub.cleaned_data.get('email')
            send_mail(subject, message, email_from, [recepient], fail_silently=False)
            return render(request, 'testapp/success.html', {'recepient': recepient})
    return render(request, 'testapp/index.html', {'form': sub})
