var map = L.map('map').setView([{{ party.location_lat }}, {{party.location_lng}}], 14);

//OSMレイヤー追加
L.tileLayer(
	'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
	{
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>',
		maxZoom: 18
	}
).addTo(map);

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
	if (this.readyState==4 && this.status==200) {
		var address_td = document.getElementById('address');
		address_td.innerHTML = this.response.address.state + ", " + this.response.address.city;
		console.log(this.response.address)
	}
};
xhr.responseType = 'json';
xhr.open('GET', 'http://nominatim.openstreetmap.org/reverse?format=json&lat='+party.location_lat+'&lon='+party.location_lng, true);
xhr.send();
