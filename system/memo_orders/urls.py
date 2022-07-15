from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('place_memo_order/', views.place_memo_order, name='place_memo_order'),
    path('place_memo_order/', MemoOrderView.as_view(), name='place_memo_order'),


    # path('memo_order_complete/', views.memo_order_complete, name='memo_order_complete'),
]
