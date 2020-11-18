from django import forms
from classes import models as model
from django.db import models

class SearchFilterForm(forms.ModelForm):
    Professor = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        model = model.Class
        fields = ['course_reference_number',
                    'name', 
                    'subject_id',
                    'number_id',
                    'CSBS_Req', 
                    'CSBS_Elec', 
                    'CSBA_Req', 
                    'CSBA_Elec', 
                    'time_start', 
                    'time_end',
                    ]
        labels = {'course_reference_number' : 'Class Reference Number',
                    'name' : 'Name',
                    'subject_id' : 'Subject',
                    'number_id' : 'Course Number',
                    'CSBS_Req' : 'CSBS Required',
                    'CSBS_Elec' : 'CSBS Elective',
                    'CSBA_Req' : 'CSBA Required',
                    'CSBA_Elec' : 'CSBA Elective',
                    'time_start' : 'Time Start',
                    'time_end' : 'Time End'}
