console.log(document.getElementById('myChart'));
var ctx = document.getElementById('myChart').getContext('2d');

var graphData = {
    type: 'line',
    data: {
        labels: ['01.07', '02.07', '03.07', '04.07', '05.07', '06.07'],
        datasets: [{
            data: [3250.2, 3340.7, 3450.2, 3703.6, 3690.5, 3201.6],
            backgroundColor: [
                'rgba(73, 198, 230, 0.5)',
            ],
            borderWidth: 1,
            borderColor: 'rgb(75, 192, 192)',
            fill: false,
            tension: 0,
        }]
    },
    options: {}
};



var myChart = new Chart(ctx, graphData);

var socket = new WebSocket('ws://localhost:8000/ws/stock/');

var old_values = graphData.data.datasets[0].data;

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);

    graphData.data.datasets[0].data = djangoData.values;
    graphData.data.labels = djangoData.date;
    if (old_values != djangoData.values) {
        myChart.update();
        old_values = djangoData.values;
    }

}