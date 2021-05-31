let REFRESH_TIMEOUT = 2500;
let $dialogMessagesDOM;

function messageRender(message) {
    let domMessage = $('.message-' + message.pk);
    let messageText;
    if (!domMessage.length) {
        let newMessage = document.createElement('li');
        newMessage.classList.add('message-' + message.pk);
        messageText = message.username + " (" + message.created + ") - " + message.text;
        newMessage.innerHTML = messageText;
        let parent = $dialogMessagesDOM.find('.messages-list');
        console.log('parent', parent);
        //[ul.messages-list, prevObject: S.fn.init(1)]
        console.log('newMessage', newMessage);
        parent.prepend(newMessage);
    }
}


window.onload = function () {
    console.log('ready');
    // $dialogMessagesDOM = document.querySelectorAll('.dialog-messages');
    $dialogMessagesDOM = $('.dialog-messages');
    // console.log('$dialogMessagesDOM', $dialogMessagesDOM);
    $dialogMessagesDOM.on('click', 'a.dialog-update', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (response) {
                let new_messages = response.new_messages;
                if (new_messages) {
                    new_messages.forEach(function (el, idx) {
                        messageRender(el);
                    })
                }
            }
        })
    });

    // setInterval(function () {
    //     console.log("update messages");
    // }, REFRESH_TIMEOUT);
    setInterval(function () {
        $('.dialog-update').trigger("click");
    }, REFRESH_TIMEOUT);
}



