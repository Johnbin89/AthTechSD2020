from django.conf.urls import url
from django.urls import path
from reporting import views as views_report

urlpatterns = [
    path('foreas_report/', views_report.report_foreas, name='report_foreas'),
    path('esyd_report/', views_report.report_esyd, name='report_esyd'),
    path('ypan_report/', views_report.report_ypan, name='report_ypan')
]
