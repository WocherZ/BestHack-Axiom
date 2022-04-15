from django.urls import path

from .consumers import WSConsumer, GraphConsumer

ws_urlpatterns = [
    path('ws/stocks/', WSConsumer.as_asgi()),
    path('ws/stock/', GraphConsumer.as_asgi())
]
