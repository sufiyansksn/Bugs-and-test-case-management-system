from django import forms

from adminsapp.models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
