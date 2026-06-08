from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'etfs', views.ETFViewSet, basename='etf')
router.register(r'dividends', views.DividendRecordViewSet, basename='dividend')

urlpatterns = [
    path('', include(router.urls)),
    path('export/excel/', views.export_etf_excel, name='export-excel'),
    path('twse/list/', views.twse_etf_list, name='twse-etf-list'),
    path('twse/import/', views.import_etfs, name='twse-import'),
]
