from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = forms.SearchFilterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        
    else:
        form = forms.SearchFilterForm()
    
    return render(request, 'add/add_home.html', {'form': form})

@login_required(login_url='login')
def results(request):
    return render(request, 'add/results.html')

@login_required(login_url='login')
def add_success(request):
    return render(request, 'add/add_success.html')