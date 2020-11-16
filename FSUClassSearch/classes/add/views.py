from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'add/add_home.html')

@login_required(login_url='login')
def results(request):
    return render(request, 'add/results.html')

@login_required(login_url='login')
def add_success(request):
    return render(request, 'add/add_success.html')