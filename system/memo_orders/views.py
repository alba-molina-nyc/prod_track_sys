from django.shortcuts import redirect
from .forms import MemoOrderForm
from memos.models import MemoItem
from .models import MemoOrder
import datetime
from django.views.generic import  CreateView

class MemoOrderView(CreateView):
    model = MemoOrder
    template_name = 'memo_orders/memo_orders.html'
    fields = '__all__'






# Create your views here.
# memo_orders aka orders
# create order 
# def place_memo_order(request):
#     current_user = request.user
#     # if memo count is less or equal to 0 then send back to list of jobs
#     memo_items = MemoItem.objects.filter(user=current_user)
#     memo_count = memo_items.count()
#     if memo_count <= 0:
#         return redirect('home') # return to the list of jobs 
    

#     if request.method == 'POST':
#         form = MemoOrderForm(request.POST) # we need to receive post from the order form
#         if form.is_valid():
#             # store all the info inside the order table
#             data = MemoOrderForm() # instance of order
#             data.setter_fname= form.cleaned_data['setter_fname']
#             data.setter_lname= form.cleaned_data['setter_lname']
#             data.setter_email= form.cleaned_data['setter_email']
#             data.note= form.cleaned_data['note']
#             data.save()
#         # generate order num
#             yr = int(datetime.date.today().strftime('%Y'))
#             dt = int(datetime.date.today().strftime('%d'))
#             mt = int(datetime.date.today().strftime('%m'))
#             d = datetime.date(yr,mt,dt)
#             current_date = d.strftime('%Y%m%d') # 20230305
#             memo_order_num = current_date + str(data.id)
#             data.memo_order_num = memo_order_num
#             data.save()

#             memo_order = MemoOrder.objects.get(is_memoed=True)
#             context = {
#                 'memo_order': memo_order,
#                 'memo_items': memo_items,
#             }
#             return render(request, 'memo_orders/.memo_orders.html', context)
#     else:
#         return redirect('checkout')

