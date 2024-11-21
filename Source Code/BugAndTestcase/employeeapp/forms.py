from django import forms

from adminsapp.models import *
from employeeapp.models import *

class TestcaseForm(forms.ModelForm):
    class Meta:
        model = Testcase
        fields = "__all__"

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = "__all__"

class RequirementsForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = "__all__"
