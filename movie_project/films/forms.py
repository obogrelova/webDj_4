from .models import Film
from django.forms import ModelForm, TextInput, Textarea

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание фильма'}),
            'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите отзыв о фильме'})
        }