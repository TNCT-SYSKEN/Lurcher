$(function() {
    $("select").selectpicker()

    $('#add-new-category').on('click', function() {
        let category = $('input[name="input-new-category"]').val()

        if(category === '') return
        $('#id_category').append(function() {
            if($('#id_category option:contains("' + category + '")').length === 0) {
                $('input[name="input-new-category"]').val('')
                return $('<option>').val($('#id_category option').length + 1).text(category)
            }
        })

        $("select").selectpicker('refresh')
    })
})