from django import forms
from . models import movie5


class MovieForm(forms.ModelForm):
    class Meta:
        model=movie5
        fields=['name','desc','year','img']