var map;

function initialize(){
    map = L.map('map').setView([59.9, 30.3], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidmxhZHV4YTIzIiwiYSI6ImNrbzA1dHV3cDBjaDIyd210Y2JzdzhrbzYifQ.Py08SB4GNGiV-grb_PvgOw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
//            id: 'mapbox/satellite-streets-v11',
//            id: 'mapbox/light-v10',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);

    new QWebChannel(qt.webChannelTransport, function (channel) {
    window.MainWindow = channel.objects.MainWindow;
    if(typeof MainWindow != 'undefined') {
        var onMapMove = function() { MainWindow.onMapMove(map.getCenter().lat, map.getCenter().lng) };
        map.on('move', onMapMove);
        onMapMove();
    }
    });


}