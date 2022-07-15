from django.urls import path
from . import views
from .views import *
# Create your views here.
# thesys aka store


urlpatterns = [
    path('', FilterByJobView.as_view(), name='job-filter'),
    path('add_job/', AddJobView.as_view(), name='add-job'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
  
   
  

]