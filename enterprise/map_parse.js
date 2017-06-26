var markers = MV.globals.gmaps[0].markers;
var marker_ids = Object.keys(MV.globals.gmaps[0].markers);
gps_data = {}
for (var i = 0; i < marker_ids.length; i++) {
    var marker = markers[marker_ids[i]];
    var marker_lat = marker.latlng.lat();
    var marker_lng = marker.latlng.lng();
    gps_data[marker_ids[i]] = {"lat" : marker_lat, "lng" : marker_lng};
}