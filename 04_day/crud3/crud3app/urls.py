from django.urls import path
from . import views

app_name = 'crud3'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create')
]
