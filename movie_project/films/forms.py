from .models import Film
from django.forms import ModelForm

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']