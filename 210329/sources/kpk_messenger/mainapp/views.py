from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from mainapp.models import Dialog, DialogMemebers, Message


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def show_dialog(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    _dialog_members = DialogMemebers.objects.filter(dialog=dialog)
        # exclude(member=request.user)
        # exclude(member_id=request.user.pk)
    dialog_members = _dialog_members.exclude(member=request.user).\
        select_related('member')
    dialog_messages = Message.objects.filter(sender__in=_dialog_members).\
        select_related('sender__member')

    # print(dialog)
    # print(dialog_members)
    # print(dialog_messages)

    context = {
        'dialog': dialog,
        'dialog_members': dialog_members,
        'dialog_messages': dialog_messages,
    }

    return render(request, 'mainapp/show_dialog.html', context)
