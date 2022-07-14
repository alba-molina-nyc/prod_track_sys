from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),#acc
    path('users/', include('users.urls')), #acc
    path('', views.home, name='home'),
    path('sys/', include('thesys.urls')),  #st
    path('memo/', include('memos.urls')), #ca
    path('memo_orders/', include('memo_orders.urls')), #or
]