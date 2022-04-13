from django.urls import path

from . import views

urlpatterns = [
    path('stocks/', views.stocks, name='stocks'),
    path('stock/<slug:stock_slug>/', views.stock, name='stock'),
]
