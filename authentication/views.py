from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants


def register(request):
    register_url = '/auth/register'

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password-confirmation')

        if password != password_confirmation:
            messages.add_message(request, constants.ERROR,
                                 'As senhas não coincidem')
            return redirect(register_url)

        if len(username.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect(register_url)

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Esse usuário já existe')
            return redirect(register_url)

        try:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Usuário criado com sucesso')

            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR,
                                 'Erro interno do sistema')
            return redirect(register_url)


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.add_message(request, constants.ERROR,
                                 'Username ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/jobs/find_jobs')


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
