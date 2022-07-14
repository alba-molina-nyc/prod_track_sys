from django.urls import path
from . import views

# Create your views here.
# thesys aka store


urlpatterns = [
    # path('', views.thesys, name='thesys'),
    path('search/', views.search, name='search'),
  
]