from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path("profile/edit/", update_profile, name="edit_profile"),
    path('profile/', profile, name="profile"),
    path("registration/", SignUp.as_view(), name="registration"),
    path("balance/", balance, name="balance"),
]
