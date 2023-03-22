from django.urls import path
from . import views

app_name = 'crud1'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('form/', views.form, name='form'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
]