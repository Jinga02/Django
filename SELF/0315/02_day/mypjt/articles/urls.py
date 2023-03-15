# from django.contrib import admin
# from django.urls import path
# from . import views

# app_name attribute를 작성해 URL namespace를 설정
# 각 app의 url마다 불러오기
# app_name = 'articles'
# {%  url'articles:index' %}
# app_name을 지정한 이후에는 url태그에 반드시 app_name:url_name형태로 사용해야한다

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("index/", views.index),
#     path('greeting/', views.greeting),
#     path('greeting2/', views.greeting2),
#     path('dinner/', views.dinner),
#     path('base/', views.base),
#     path('child/', views.child),
# ]
