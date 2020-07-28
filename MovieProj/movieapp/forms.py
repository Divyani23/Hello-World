from movieapp.models import AbtMovie
from django import forms

class AbtMovieForm(forms.ModelForm):
    class Meta:
        model=AbtMovie
        fields='__all__'
