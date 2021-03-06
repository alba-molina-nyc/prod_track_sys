from django.urls import path
from . import views


urlpatterns = [
    path('', views.memo, name='memo'),
    path('add_memo/<int:job_id>/', views.add_memo, name='add_memo'),
    path('remove_memo_item/<int:job_id>/<int:memo_item_id>/', views.remove_memo_item, name='remove_memo_item'),

    path('checkout/', views.checkout, name='checkout'),
]