$(function() {
    let date, time

    /** マップ **/
    /* 確定ボタンを押すと緯度・経度を非表示インプットに挿入 */
    $(document).on('click', '#set-latlng', function() {
        let latlng = marker.getLatLng()
        $('input:hidden[name="location_lat"]').val(latlng.lat)
        $('input:hidden[name="location_lng"]').val(latlng.lng)
        $('input:text[name="location-status"]').val('設定済み')
    })

    /** 開催日時 **/
    /* 日付と時間を結合して非表示インプットに挿入(JST) */
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
