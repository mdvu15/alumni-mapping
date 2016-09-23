var map = L.map('map').setView([39.48, -84.45], 5);
var myURL = jQuery( 'script[src$="map-leaf.js"]' ).attr( 'src' ).replace( 'map-leaf.js', '' );

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
			attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>' +
				 		 'contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">' +
				 		 'CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
			maxZoom: 18,
			id: 'kmmuterspaw.o00h3fho',
			accessToken: 'pk.eyJ1Ijoia21tdXRlcnNwYXciLCJhIjoiREdzandMMCJ9.YtGf8S1_imPsZKBhTAKEsg'
}).addTo(map);

var circle = L.circle([39.48, -84.45], 10000, {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5
}).addTo(map);

circle.bindPopup("<b>I am a Circle!!!</b>");