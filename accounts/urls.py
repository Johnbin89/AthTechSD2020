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
    path('foreas_profile/<user_id>', views_accounts.ForeasProfile.as_view() , name='foreas_profile'),
    path('ypan_profile/<user_id>', views_accounts.YpAnProfile.as_view() , name='ypan_profile'),
    path('esyd_profile/<user_id>', views_accounts.EsydProfile.as_view() , name='esyd_profile'),
    path('regulation/',views_accounts.regulation_view, name='regulation'),
    # path('regulation_selection/', views_accounts.regulation_selection, name='regulation_selection'),
    path('new_regulation/',views_accounts.NewRegulation.as_view(),name='new_regulation'),
    path('new_subfield/',views_accounts.NewSubField.as_view(),name='new_subfield')
]

#urlpatterns += staticfiles_urlpatterns()