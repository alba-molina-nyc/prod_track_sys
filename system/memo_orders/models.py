from django.db import models
from users.models import User
from thesys.models import Job

# Create your models here.

# create order model
class MemoOrder(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    memo_order_number = models.CharField(max_length=20, default=None)
    setter_fname = models.CharField(max_length=250, blank=True)
    setter_lname = models.CharField(max_length=250, blank=True)
    setter_email = models.EmailField(max_length=50)
    note = models.CharField(max_length=100, blank=True)
    order_total = models.FloatField()
    is_memoed = models.BooleanField(default=False) #only has been assigned when setter receives it
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    creator_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



    

   


   

 