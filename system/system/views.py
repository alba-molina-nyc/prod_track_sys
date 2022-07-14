from django.shortcuts import render
from thesys.models import Job

def home(request):
    jobs = Job.objects.all()

    # Get the reviews
    reviews = None
    for job in jobs:
        job

    context = {
        'jobs': jobs,

    }
    return render(request, 'home.html', context)