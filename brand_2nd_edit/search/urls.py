from django.urls import path 
from . import views

urlpatterns = [
    path('', views.search, name = 'search'),
    #path(r'^(?P<comp_id>[0-9]+)/$', views.detail, name = 'detail'),
    path('company/<int:comp_id>/', views.detail, name = 'detail'),
    path(r'^result/(?P<brand_name>\w+?)/$', views.result, name = 'result'),
    path('brand/<int:brand_id>/', views.brand_info, name = 'brand_info')

    #path('result/', views.result, name = 'result')
]