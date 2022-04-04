from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password-confirmation')


def login(request):
    return HttpResponse('Login')
