from django import forms
from .models import StudentProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['profile_picture']
