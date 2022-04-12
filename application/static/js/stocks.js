var socket = new WebSocket('ws://localhost:8000/ws/stocks/');

socket.onmessage = function(event) {
    let data = JSON.parse(event.data);
    let list = data.list_stocks;
    let index;
    let parent = document.querySelector('#parent');
    for (index = 0; index < list.length; ++index) {
        let name = String(list[index].name)
        let price = String(list[index].price)
        let find_stock = document.getElementById('stock_' + name);
        if (find_stock) {
            find_stock.innerHTML = name + ' ' + price;
        } else {
            let div = document.createElement('div');
            div.id = 'stock_' +name;
            div.innerHTML = name + ' ' + price;
            parent.appendChild(div);
        }
    }
}