from django.db import models
from django.contrib.auth.models import User
from thesys.models import Job


class Memo(models.Model): #ca
    memo_id = models.CharField(max_length=250, blank=True)
    date_set = models.DateField(auto_now_add=True)
   
    
    def __str__(self):
        return self.memo_id


class MemoItem(models.Model): #caitem
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.job.num_stones * 0.50
