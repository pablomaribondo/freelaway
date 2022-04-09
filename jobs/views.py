from django.shortcuts import render, redirect
from .models import Job
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


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


def profile(request):
    if request.method == "GET":
        return render(request, 'profile.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        profile_url = '/jobs/profile'

        user = User.objects.filter(
            username=username).exclude(id=request.user.id)

        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usuário com esse Username')
            return redirect(profile_url)

        user = User.objects.filter(email=email).exclude(id=request.user.id)

        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usuário com esse E-mail')
            return redirect(profile_url)

        request.user.username = username
        request.user.email = email
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        messages.add_message(request, constants.SUCCESS,
                             'Dados alterados com sucesso')
        return redirect(profile_url)
