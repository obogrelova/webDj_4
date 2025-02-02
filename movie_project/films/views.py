from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', {'films': films})

def add_new_movie(request):
    error = ""
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были заполнены некорректно"
    form = FilmForm()

    return render(request, 'films/add_new_movie.html', {'form': form, 'error': error})

