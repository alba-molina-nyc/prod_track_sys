from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from memos.models import MemoItem
from django.db.models import Q
from memos.views import _memo_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            jobs = Job.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(job_name__icontains=keyword))
            job_count = jobs.count()
    context = {
        'jobs': jobs,
        'job_count': job_count,
    }
    return render(request, 'thesys/thesys.html', context)
