from django.urls import path 
from . import views

urlpatterns = [
    path('', views.search, name = 'search'),
    path('<int:comp_id>/', views.detail, name = 'detail'),
    path(r'^result/(?P<brand_name>\w+?)/$', views.result, name = 'result')

    #path('result/', views.result, name = 'result')
]