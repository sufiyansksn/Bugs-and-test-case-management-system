from django import forms

from managementapp.models import *
#from employeeapp.models import BugForm,TestcaseForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
