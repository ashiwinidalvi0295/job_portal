from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jobapp.models import ITJobs, MechJobs, CivilJobs, UserData

class user_profile_view(forms.ModelForm):
    class Meta:
        model = UserData
        fields = "__all__"

class add_it_job_form(forms.ModelForm):
    class Meta:
        model   =   ITJobs
        fields  =   "__all__"
        widgets =   {
            'Mod_date' : forms.DateInput(attrs={'type': 'date'}),
            'last_date' : forms.DateInput(attrs={'type': 'date'})
        }
    def __str__(self):
        return self.company_name

class update_it_job_form(forms.ModelForm):
    class Meta:
        model   =   ITJobs
        fields  =   "__all__"
        widgets =   {
            'Mod_date' : forms.DateInput(attrs={'type': 'date'}),
            'last_date' : forms.DateInput(attrs={'type': 'date'})
        }
    def __str__(self):
        return self.company_name

class add_mech_job_form(forms.ModelForm):
    class Meta:
        model   =   MechJobs
        fields  =   "__all__"
        widgets =   {
            'Mod_date' : forms.DateInput(attrs={'type': 'date'}),
            'last_date' : forms.DateInput(attrs={'type': 'date'})
        }
    def __str__(self):
        return self.company_name

class update_mech_job_form(forms.ModelForm):
    class Meta:
        model   =   MechJobs
        fields  =   "__all__"
        widgets =   {
            'Mod_date' : forms.DateInput(attrs={'type': 'date'}),
            'last_date' : forms.DateInput(attrs={'type': 'date'})
        }
    def __str__(self):
        return self.company_name

class add_civil_job_form(forms.ModelForm):
    class Meta:
        model   =   CivilJobs
        fields  =   "__all__"
        widgets =   {
            'Mod_date' : forms.DateInput(attrs={'type': 'date'}),
            'last_date' : forms.DateInput(attrs={'type': 'date'})
        }
    def __str__(self):
        return self.company_name

class update_civil_job_form(forms.ModelForm):
    class Meta:
        model   =   CivilJobs
        fields  =   "__all__"
        widgets =   {
            'Mod_date' : forms.DateInput(attrs={'type': 'date'}),
            'last_date' : forms.DateInput(attrs={'type': 'date'})
        }
    def __str__(self):
        return self.company_name

class user_reg(UserCreationForm):
    class Meta:
        model   = User
        fields  = ['username','email','password1','password2']
