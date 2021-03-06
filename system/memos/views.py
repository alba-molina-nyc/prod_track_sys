#memos aka carts
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, MemoItem, Memo
from django.core.exceptions import ObjectDoesNotExist
from .filters import MemoFilter
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# create private function from this request we are going to take the memo.id
def _memo_id(request):
    # session_key -> session_id,
    memo = request.session.session_key
    if not memo:
        memo = request.session.create()
    # return the memo & memo id
    return memo

# decrement and remove memoItem aka job by 1
def remove_memo_item(request, job_id):
    memo = Memo.objects.get(memo_id=_memo_id(request))
    job = get_object_or_404(Job, id=job_id)
    memo_item = MemoItem.objects.get(job=job, memo=memo)
    memo_item.delete()
    return redirect('memo')

# add job inside the memo, so need job_id
def add_memo(request, job_id):
    job = Job.objects.get(id=job_id) #get the job
    try: 
        memo = Memo.objects.get(memo_id=_memo_id(request)) # the memo using the memo_id present in the session
    except Memo.DoesNotExist:
        memo = Memo.objects.create(
            memo_id = _memo_id(request)
        )
    memo.save() # up to this point we have a job and the cart put the job inside the cart, the job becomes cartItem

    try:
        memo_item = MemoItem.objects.get(job=job, memo=memo)
        memo_item.quantity += 1 # want to increment memo by 1
        memo_item.save()
    except MemoItem.DoesNotExist:
        memo_item = MemoItem.objects.create(
            job = job,# pass in which job should be in the memo
            quantity = 1,
            memo = memo, # we now create the cart 
        )
        memo_item.save() # save the memoitem
   
    return redirect('memo') # redirect the user to the memo page

def memo(request, total= 0, quantity=0, memo_items=None): 
    try: 
        memo = Memo.objects.get(memo_id=_memo_id(request))
        memo_items = MemoItem.objects.filter(memo=memo, is_active=True)

        for memo_item in memo_items:
            total += memo_item.job.num_stones * 0.50
            quantity += memo_item.quantity

    except ObjectDoesNotExist: # but if the memo_item does not exst pass
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'memo_items': memo_items,
    }
    return render(request, 'memos/memo.html', context)


def checkout(request,total= 0, quantity=0, memo_items=None): 
    try: 
        memo = Memo.objects.get(memo_id=_memo_id(request))
        memo_items = MemoItem.objects.filter(memo=memo, is_active=True)
        print(memo, 'try clause')

        for memo_item in memo_items:
            total += memo_item.job.num_stones * 0.50
            quantity += memo_item.quantity
            print(total, 'try memo')

    except ObjectDoesNotExist: # but if the memo_item does not exst pass
        print(memo, 'except')
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'memo_items': memo_items,
    }
    # return render(request, 'memos/checkout.html' ,context)
    return render(request, 'memos/checkout.html' ,context)









# class FilterByMemoView(ListView):
#     model = Memo
#     filter = MemoFilter
#     template_name = 'memos/memo.html'
#     fields = '__all__'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = MemoFilter(self.request.GET, queryset=self.get_queryset())
#         return context









    # http://localhost:8000/memo/ -  render(request, 'memos/memo.html', context)