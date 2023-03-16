from django.contrib import admin
from django.urls import path
from articles import views
# from pages import views as pages_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.index),
    path('greeting/', views.greeting),
    path('greeting2/', views.greeting2),
    # <a href="{% url 'dinner' %}">dinner 바로가기</a>
    path('dinner/', views.dinner, name='dinner'),
    path('base/', views.base),
    path('child/', views.child),
    # path('index/', pages_views.index),
]
# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#     path('artilces/', include('articles.urls')),
#     path('pages/', include('pages.urls')),
# ]