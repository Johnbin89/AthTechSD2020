from django.conf.urls import url
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LoginView
from django.urls import path

from . import views as views_app

urlpatterns = [
    path('', views_app.index, name='index'),
    #url(r'^login/$', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('login/', views_app.login, name='login'),
    path('register/', views_app.register, name='register'),
    # url(r'^logout/$', auth_views.LoginView.as_view(), name='logout')
]