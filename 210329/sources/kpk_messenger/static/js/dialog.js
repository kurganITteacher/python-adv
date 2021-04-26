let $dialogMessagesDOM;

function messageRender(message) {
    let domMessage = $('.message-' + message.pk);
    let messageText;
    if (!domMessage.length) {
        //<li class="message-{{ item.pk }}">
        //     {{ item.sender.member.username }}
        //     ({{ item.created|date:"Y.m.d H:i" }}) - {{ item.text }}
        // </li>
        let newMessage = document.createElement('li');
        newMessage.classList.add('message-' + message.pk);
        messageText = message.username + " (" + message.created + ") - " + message.text;
        newMessage.innerHTML = messageText;
        let parent = $dialogMessagesDOM.find('.messages-list');
        parent.prepend(newMessage);
        // console.log('parent', parent);
        // console.log('to render', message, newMessage, messageText);
    }
}


window.onload = function () {
    console.log('ready');
    $dialogMessagesDOM = $('.dialog-messages');
    $dialogMessagesDOM.on('click', 'a.dialog-update', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (response) {
                // console.log(response);
                // $('.card').update();
                let new_messages = response.new_messages
                if (new_messages) {
                    new_messages.forEach(function (el, idx) {
                        // console.log(idx, el);
                        messageRender(el);
                    })
                }
            }
        })
    })
}



