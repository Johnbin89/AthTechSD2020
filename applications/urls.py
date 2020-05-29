from django.conf.urls import url
from django.urls import path
from applications import views as views_applications

urlpatterns = [
    path('foreas-esyd/', views_applications.esyd_for_foreas, name='esyd_for_foreas'),
    path('xeiristis-esyd/', views_applications.esyd_xeiristis, name='esyd_xeiristis'),
    path('ypan_application/', views_applications.ypan_application, name='ypan_application'),
    path('home/', views_applications.user_home, name='user_home_page'),
    path('updatetest/', views_applications.updateSub_onEsyd, name='esyd_update_subfield')
]
