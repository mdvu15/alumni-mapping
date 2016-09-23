var map = L.map('map').setView([39.48, -84.45], 4);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>' +
				 'contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">' +
				 'CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	maxZoom: 18,
	id: 'kmmuterspaw.o00h3fho',
	accessToken: 'pk.eyJ1Ijoia21tdXRlcnNwYXciLCJhIjoiREdzandMMCJ9.YtGf8S1_imPsZKBhTAKEsg'
	}).addTo(map);

	$.getJSON(Flask.url_for("static", {"filename":"js/alums.geojson"}),function(data){
		var alums = L.geoJson(data,{
		pointToLayer: function(feature,latlng) {
			var marker = L.marker(latlng);
			marker.bindPopup(feature.properties.Zipcode);
			return marker;
		}
		});

		var clusters = L.markerClusterGroup();
		clusters.addLayer(alums);
		map.addLayer(clusters);
		map.addControl( searchControl );
	});
