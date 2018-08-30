var map = L.map('type').setView([35.710063, 139.8107], 16);
var tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    maxZoom: 19
});
tileLayer.addTo(map);

var marker = L.marker([35.710063, 139.8107], { 'draggable': 'true' }).addTo(map);

var popup = L.popup();
var content = '<div class="text-center"><p>ここで確定しますか？</p><button id="set-latlng" class="btn btn-primary" type="button">確定</button></div>'

marker.on('click', function() {
    popup.setLatLng(marker.getLatLng())
        .setContent(content)
        .openOn(map)
})