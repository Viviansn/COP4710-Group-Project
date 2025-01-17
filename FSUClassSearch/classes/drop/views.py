from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'drop/drop_home.html')

@login_required(login_url='login')
def drop_success(request):
    return render(request, 'drop/drop_success.html')
