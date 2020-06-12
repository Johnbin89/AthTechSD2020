from django.conf.urls import url
from django.urls import path
from applications import views as views_applications

urlpatterns = [
    path('foreas-esyd/', views_applications.esyd_for_foreas, name='esyd_for_foreas'),
    path('xeiristis-esyd/', views_applications.esyd_xeiristis, name='esyd_xeiristis'),
    path('ypan_application/', views_applications.ypan_application, name='ypan_application'),
    path('xeiristis-ypan/', views_applications.ypan_xeiristis, name='ypan_xeiristis'),
    path('home/', views_applications.user_home, name='user_home_page'),
    path('updatetest/', views_applications.updateSub_onEsyd, name='esyd_update_subfield'),
    path('updateYpan/', views_applications.updateSub_onYpan, name='ypan_update_subfield')
]
