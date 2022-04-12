import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

from .models import Stock


class WSConsumer(WebsocketConsumer):
    def connect(self):
        print("WebSocket connect")
        self.accept()

        for i in range(100):
            data_stocks = []
            for stock in Stock.objects.all():
                data_stocks.append({
                    'name': stock.name,
                    'price': float(stock.current_price)
                })
            self.send(json.dumps({'list_stocks': data_stocks}))
            sleep(1)

    def disconnect(self, code):
        print("WebSocket disconnect")
