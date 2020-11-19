from django import forms
from classes import models as model
from django.db import models

class SearchFilterForm(forms.Form):
    subject_id = forms.CharField(max_length=6, label='Subject', required=False)
    number_id = forms.CharField(max_length=4, label='Course Number', required=False)
    name = forms.CharField(max_length=60, label='Course Name', required=False)
    course_reference_number = forms.CharField(max_length=6, label='Class Reference Number', required=False)
    professor = forms.CharField(max_length=50, label='Professor', required=False)
    time_start = forms.TimeField(label='Time Start', required=False)
    time_end = forms.TimeField(label='Time End', required=False)
    keywords = forms.CharField(max_length=60, label='Key Words', required=False)
    CSBS_Req = forms.BooleanField(label='CSBS Required', required=False)
    CSBS_Elec = forms.BooleanField(label='CSBS Elective', required=False)
    CSBA_Req = forms.BooleanField(label='CSBA Required', required=False)
    CSBA_Elec = forms.BooleanField(label='CSBA Elective', required=False)
    
    
    
    
    
    
    """
    def __init__(self, *args, **kwargs):
        super(SearchFilterForm, self).__init__(*args, **kwargs)
        self.fields['course_reference_number'].required = False
        self.fields['name'].required = False
        self.fields['subject_id'].required = False
        self.fields['number_id'].required = False
        #self.fields['Professor'].required = False
        
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
    
    def save(self, commit=True):
        return super(SearchFilterForm, self).save(commit=commit)

    """
