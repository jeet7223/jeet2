from django import forms
from project_app.models import user

class myform(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"
