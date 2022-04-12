from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Stock, Properties


def home(request):
    return render(request, 'home.html')


def stocks(request):
    return render(request, 'stocks.html')


def stock(request, stock_slug):
    stock_object = get_object_or_404(Stock, slug=stock_slug)
    return HttpResponse("Your slug:" + str(stock_object.slug))
