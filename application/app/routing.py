from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/stocks/', WSConsumer.as_asgi())
]
