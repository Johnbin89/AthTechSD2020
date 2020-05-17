from django.conf.urls import url
# from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LoginView
from django.urls import path
from app import views as views_app
#from accounts import views as views_accounts

urlpatterns = [
    path('', views_app.index, name='index'),
    path('services/', views_app.services, name='services'),
    path('contactus/', views_app.contactus, name='contactus')
    # path('login/', LoginView.as_view(extra_context={'login': True}), name='login'),
    # path('register/', views_accounts.register, name='register'),
    # path('logout/', views_accounts.logout_view, name='logout')
]
