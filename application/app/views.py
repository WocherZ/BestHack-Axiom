from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import *


def stocks(request):
    return render(request, 'stocks.html')


def stock(request, stock_slug):
    stock_object = get_object_or_404(Stock, slug=stock_slug)
    return HttpResponse("Your slug:" + str(stock_object.slug))


def home(request):
    return render(request, "home.html")


def profile(request):
    return render(request, "profile.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"


@login_required
@transaction.atomic
def balance(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            user = User.objects.all().get(id=request.user.id)
            user.profile.balance = request.user.profile.balance + user.profile.balance
            user.save()
            messages.success(request, ('Баланс пополнен.'))
            return redirect('profile')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'balance.html', {'profile_form': profile_form})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('profile')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
    })
