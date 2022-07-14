from django.contrib import admin
from .models import MemoItem,Memo

admin.site.register(Memo)
admin.site.register(MemoItem)
