# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from app import views as views_app
from accounts import views as views_accounts
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'regulation', views_accounts.RegulationViewSet)
router.register(r'subfield', views_accounts.SubFieldViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(extra_context={'login': True}), name='login'),
    path('foreas_demo_login/', views_accounts.foreas_login, name='foreas_demo_login'),
    path('esyd_demo_login/', views_accounts.esyd_login, name='esyd_demo_login'),
    path('ypan_demo_login/', views_accounts.ypan_login, name='ypan_demo_login'),
    path('register/', views_accounts.register, name='register'),
    path('logout/', views_accounts.logout_view, name='logout'),
    path('foreas_profile/<user_id>', views_accounts.ForeasProfile.as_view() , name='foreas_profile'),
    path('ypan_profile/<user_id>', views_accounts.YpAnProfile.as_view() , name='ypan_profile'),
    path('esyd_profile/<user_id>', views_accounts.EsydProfile.as_view() , name='esyd_profile'),
    path('regulation/',views_accounts.regulation_view, name='regulation'),
    # path('regulation_selection/', views_accounts.regulation_selection, name='regulation_selection'),
    path('new_regulation/',views_accounts.NewRegulation.as_view(),name='new_regulation'),
    path('new_subfield/',views_accounts.NewSubField.as_view(),name='new_subfield'),

    #Some experiments on Django REST framework
    path('api/', include(router.urls)),
    path('api-auth/logout', views_accounts.logout_view, name='rest_framework_logout'), #overried logout before api-auth/ makes POST logout
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

#urlpatterns += staticfiles_urlpatterns()