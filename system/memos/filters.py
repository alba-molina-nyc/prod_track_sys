import django_filters
from .models import Memo

class MemoFilter(django_filters.FilterSet):
    class Meta: 
        model = Memo
        fields = '__all__'
