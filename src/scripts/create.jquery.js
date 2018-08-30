$(function() {
    $("select").selectpicker()

    /* 新規カテゴリ作成でセレクトに追加 */
    $('#add-new-category').on('click', function() {
        let category = $('input[name="input-new-category"]').val()

        if(category === '') return
        $('#id_category').append(function() {
            if($('#id_category option:contains("' + category + '")').length === 0) {
                $('input[name="input-new-category"]').val('')
                return $('<option>').val($('#id_category option').length + 1).text(category)
            }
        })

        /* APIでカテゴリを追加 */
        $.ajax({
            url: '/api/categories/',
            type: 'POST',
            headers: {
                'X-CSRFTOKEN': Cookies.get('csrftoken'),
            },
            data: {
                'category': category
            }
        }).fail(response => {
            alert('エラーが発生しました')
        })

        $("select").selectpicker('refresh')
    })
})