from django.shortcuts import render, redirect
from .forms import InstaRegistrationForm, BotRequestForm

# Create your views here.


def InstaRegistrationView(request):
    if request.method == 'POST':
        form = InstaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
        else:
            return render(request, 'registration.html')
    return render(request, 'registration.html')


def BotRequestProfileView(request):
    if request.method == 'POST':
        form = BotRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bot_request')
        else:
            return render(request, 'bot_request.html')
    return render(request, 'bot_request.html')

def HomeView(request):
    
    return render(request, 'home.html')