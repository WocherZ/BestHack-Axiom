from django.shortcuts import render, get_object_or_404
from .models import User, Stock, Properties


def home(request):
    return render(request, 'home.html')


def stock(request, stock_slug):
    slug = get_object_or_404(Stock, slug=stock_slug)
    pass
