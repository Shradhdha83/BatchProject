from django import forms
from django.db import models
from django.db.models import fields
from myapp.models import notes, signup


class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'