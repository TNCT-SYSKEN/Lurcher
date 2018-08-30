$(function() {
    let date, time

    /** マップ **/
    $(document).on('click', '#set-latlng', function() {
        let latlng = marker.getLatLng()
        $('input:hidden[name="location_lat"]').val(latlng.lat)
        $('input:hidden[name="location_lng"]').val(latlng.lng)
    })

    /** 開催日時 **/
    $('input[name="hold-date"]').on('change', function() {
        date = $('input[name="hold-date"]').val()
        setAtTime()
    })
    $('input[name="hold-time"]').on('change', function() {
        time = $('input[name="hold-time"]').val()
        setAtTime()
    })

    function setAtTime() {
        let datetime = date + ' ' + time
        $('input:hidden[name="at_time"]').val(datetime)
    }
})
