var map = L.map('type').setView([35.710063, 139.8107], 16);
var tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    maxZoom: 19
});

tileLayer.addTo(map);

var marker = L.marker([35.710063, 139.8107], { 'draggable': 'true' }).addTo(map);
marker.on('moveend', function () {
    console.log(marker.getLatLng());
});

var popup = L.popup();
function onMarker2Click(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("<p>確定しますか？</p>")
        .openOn(map);
}
map.on('click', onMarker2Click);
