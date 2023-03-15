from django.urls import path
from . import views # from 내 위치에 있는 views 가져와
urlpatterns = [
    path('hello/<str:name>', views.hello),
]