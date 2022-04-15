from django.urls import path
from .views import *

urlpatterns = [
    path('stocks/', stocks, name='stocks'),
    path('stock/<slug:stock_slug>/', stock, name='stock'),
    path('', home, name="home"),
    path("profile/edit/", update_profile, name="edit_profile"),
    path('profile/', profile, name="profile"),
    path("registration/", SignUp.as_view(), name="registration"),
    path("balance/", balance, name="balance"),
]