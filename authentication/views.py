from django.shortcuts import render, redirect
from django.http import HttpResponse


def register(request):
    register_url = '/auth/register'

    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password-confirmation')

        if password != password_confirmation:
            return redirect(register_url)

        if len(username.strip()) == 0 or len(password.strip()) == 0:
            return redirect(register_url)

def login(request):
    return HttpResponse('Login')
