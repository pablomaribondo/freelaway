from django.shortcuts import render
from .models import Job


def find_jobs(request):
    if request.method == "GET":
        jobs = Job.objects.filter(reserved=False)
        return render(request, 'find_jobs.html', {'jobs': jobs})
