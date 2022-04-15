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
            // find_stock.innerHTML = name + ' ' + price;

        } else {
            let li_element = document.createElement('li');
            li_element.id = 'stock_' + name;
            li_element.style.marginBottom = '10px';
            li_element.innerHTML = `<button id='stock_button_${name}' style='width: 100%; border-radius: 20px' 
            class='btn btn-warning me-2'>`;
            parent.appendChild(li_element);

            let stock_button = document.getElementById('stock_button_' + name);
            stock_button.innerHTML = `<div class='row' style='padding: 10px'>
                        <div class='col-6' style=' display:flex; justify-content: left'>
                            <h2>${name}</h2>
                        </div>
                        <div class='col-6' style=' display:flex; justify-content: right'>
                            <h2>${price} рублей</h2>
                        </div>
            `;

        }
    }
}