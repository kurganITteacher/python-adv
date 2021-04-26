window.onload = function () {
    console.log('ready');
    $('.dialog-messages').on('click', 'a.dialog-update', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (response) {
                console.log(response);
                // $('.card').update();
            }
        })
    })
}



