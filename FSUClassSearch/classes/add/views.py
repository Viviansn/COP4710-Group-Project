from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from django.db import connection
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = forms.SearchFilterForm(request.POST)
        if form.is_valid():
            #valid_form = form
            all_fields = get_all_fields_from_form(forms.SearchFilterForm())
            for field in get_all_fields_from_form(forms.SearchFilterForm()):
                print(field, form.cleaned_data[field])
                if form.cleaned_data[field] == "":
                    all_fields.remove(field)
                #if 
            
            print('all_fields = ', all_fields)
            #print(form.cleaned_data['name'])
            # query database results here
        
    else:
        form = forms.SearchFilterForm()
    
    return render(request, 'add/add_home.html', {'form': form})


def get_all_fields_from_form(instance):
    fields = list(instance.base_fields)
    for field in list(instance.declared_fields):
        if field not in fields:
            fields.append(field)
    
    return fields

@login_required(login_url='login')
def results(request):
    
    s = "COP"
    row = None
    with connection.cursor() as cursor:
        cursor.execute("SELECT subject_id, number_id FROM classes_class WHERE subject_id = %s", [s])
        row = dictfetchall(cursor)
    
    print(row)
    
    return render(request, 'add/results.html')


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@login_required(login_url='login')
def add_success(request):
    return render(request, 'add/add_success.html')