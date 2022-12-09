from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def sign_in(request):
    print(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('library')
                else:
                    return HttpResponse("Аккаунт неактивирован")
            else:
                return HttpResponse("Неправильные данные пользователя")

    else:
        form = LoginForm()
    return render(request, 'account/account.html', {"form": form})