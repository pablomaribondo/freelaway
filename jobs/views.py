from django.shortcuts import render


def find_jobs(request):
    return render(request, 'find_jobs.html')
