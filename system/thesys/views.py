from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Job
from .filters import JobFilter
from .forms import JobSelectForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from memos.models import Memo, MemoItem

def job_detail(request, job_slug):
    try:
        single_job = Job.objects.get(slug=job_slug)
        in_memo = MemoItem.objects.filter(memo__memo_id=_memo_id(request), job=single_job).exists()
    except Exception as e:
        raise e



    context = {
        'single_job': single_job,
        'in_memo'       : in_memo,

    }
    return render(request, 'job_detail.html', context)

def thesys(request):
    jobs = Job.objects.all().filter()
    context = {
        'jobs': jobs,
    }
    return render(request, 'system.html', context )

class HomeView(ListView):
    model = Job
    filter = JobFilter
    template_name = 'home.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    fields = '__all__'


class AddJobView(PermissionRequiredMixin, CreateView):
    permission_required = 'jobs.add_jobs'
    model = Job
    template_name = 'add_job.html'
    fields = '__all__'


class FilterByJobView(ListView):
    model = Job
    filter = JobFilter
    template_name = 'system.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context
    def SelectJob(self, request):
        job_list = JobFilter(self.request.GET, queryset=self.get_queryset())

        if request.method == 'POST':
            form = JobSelectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'system.html')
        print(form)
        return render(request, {'form' : form})

