"""self01pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from self01app import views as self01app_views
from articles import views as articles_views

# app 마다 호출 
# from articles import views as articles_views # articles app의 views를 import해라.
# path('hello/', articles_views.hello), # articles app의  views의 함수 hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('self01/', self01app_views.self01),
    path('self02/', self01app_views.self02),
    path('self03/', self01app_views.self03), # self01app app의 views의 함수 self03
    path('articles/', include('articles.urls')), # articles/로 들어오면 그 아래부터는 articles.urls로 가서 처리해 
    # path('hello/<str:name>', articles_views.hello), # hello/jaehwan jaehwan에게 hello페이지를 제공 hello/다음에 str로 들어오면 articles~~에 보내서 처리
]

