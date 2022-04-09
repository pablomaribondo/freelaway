from django.shortcuts import render, redirect
from .models import Job
from datetime import datetime


def find_jobs(request):
    if request.method == "GET":
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        min_deadline = request.GET.get('min_deadline')
        max_deadline = request.GET.get('max_deadline')

        category = request.GET.get('category')

        if min_price or max_price or min_deadline or max_deadline or category:
            if not min_price:
                min_price = 0

            if not max_price:
                max_price = 999999

            if not min_deadline:
                min_deadline = datetime(year=1900, month=1, day=1)

            if not max_deadline:
                max_deadline = datetime(year=3000, month=1, day=1)

            category = [category, ]

            jobs = Job.objects.filter(price__gte=min_price)\
                .filter(price__lte=max_price)\
                .filter(deadline__gte=min_deadline)\
                .filter(deadline__lte=max_deadline)\
                .filter(category__in=category)\
                .filter(reserved=False)
        else:
            jobs = Job.objects.filter(reserved=False)

        return render(request, 'find_jobs.html', {'jobs': jobs})


def accept_job(request, id):
    job = Job.objects.get(id=id)
    job.professional = request.user
    job.reserved = True
    job.save()

    return redirect('/jobs/find_jobs')
