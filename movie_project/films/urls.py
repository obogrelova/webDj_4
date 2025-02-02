from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_new_movie/', views.add_new_movie, name='page2')
]