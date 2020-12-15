from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^view_stock', views.view_stock, name='view_stock'),
    url(r'^$', views.index, name='index'),
    url(r'^help', views.help_page, name='help'),
    url(r'stock_detail/', views.form_name_view, name='stock_detail')
]
