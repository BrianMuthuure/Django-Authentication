from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserLoginForm, UserRegistration


def home(request):
    return render(request, 'accounts/home.html')


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

