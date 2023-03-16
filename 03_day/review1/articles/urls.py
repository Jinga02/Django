from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]