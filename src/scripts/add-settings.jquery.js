$(function() {
    $(document).on('click', '#set-latlng', function() {
        let latlng = marker.getLatLng()
        $('input:hidden[name="location_lat"]').val(latlng.lat)
        $('input:hidden[name="location_lng"]').val(latlng.lng)
    })
})