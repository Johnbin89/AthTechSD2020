from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views as views_app

urlpatterns = [
    path('', views_app.index, name='index'),
    path('login/', LoginView.as_view(extra_context = {'login': True}), name='login'),
    path('register/', views_app.register, name='register'),
    path('logout/', views_app.logout_view, name='logout')
]