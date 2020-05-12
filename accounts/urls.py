from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from app import views as views_app
from accounts import views as views_accounts

urlpatterns = [
    path('login/', LoginView.as_view(extra_context={'login': True}), name='login'),
    path('register/', views_accounts.register, name='register'),
    path('logout/', views_accounts.logout_view, name='logout'),
    path('profile/(?P<user_id>\d+/', views_accounts.ProfileForm.as_view() , name='profile'),
    path('application/', views_accounts.logout_view, name='application'),
    path('regulation/',views_accounts.regulation_view, name='regulation'),
    path('new_regulation/',views_accounts.NewRegulation.as_view(),name='new_regulation'),
    path('new_subfield/',views_accounts.NewSubField.as_view(),name='new_subfield')
]

#urlpatterns += staticfiles_urlpatterns()