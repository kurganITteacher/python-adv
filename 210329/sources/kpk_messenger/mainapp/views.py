from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from mainapp.models import Dialog, DialogMemebers, Message


@login_required
def index(request):
    dialogues = request.user.dialogs.select_related('dialog').all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def dialog_show(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    _dialog_members = DialogMemebers.objects.filter(dialog=dialog)
    dialog_members = _dialog_members.exclude(member=request.user). \
        select_related('member')
    dialog_messages = Message.objects.filter(sender__in=_dialog_members). \
        select_related('sender__member')

    context = {
        'page_title': 'диалог',
        'dialog': dialog,
        'dialog_members': dialog_members,
        'dialog_messages': dialog_messages,
    }

    return render(request, 'mainapp/dialog_show.html', context)


def dialog_create(request):
    # dialogues = DialogMemebers.objects.filter(member=request.user). \
    #     values_list('dialog_id', flat=True)
    dialogues = request.user.dialogs.select_related('dialog').all(). \
        values_list('dialog_id', flat=True)
        # values('dialog_id', 'member_id')
        # values_list('dialog_id', 'member_id')
        # values_list('dialog_id', flat=True)
    # print(dialogues)  # [20, 11, 10, 1]
    # print(dialogues)  # [(20, 2), (11, 2), (10, 2), (1, 2)]
    # print(dialogues)  # [{'dialog_id': 20, 'member_id': 2}, {'dialog_id': 11, 'member_id': 2}, {'dialog_id': 10, 'member_id': 2}, {'dialog_id': 1, 'member_id': 2}]
    interlocutors = DialogMemebers.objects.filter(dialog__in=dialogues).\
        values_list('member_id', flat=True)
        # exclude(member=request.user).\
    new_interlocutors = User.objects.exclude(pk__in=interlocutors)
    # print(new_interlocutors)

    context = {
        'page_title': 'новый диалог',
        'new_interlocutors': new_interlocutors,
    }
    return render(request, 'mainapp/dialog_create.html', context)

