from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
    dialogues = request.user.dialogs.select_related('dialog').all(). \
        values_list('dialog_id', flat=True)
    interlocutors = DialogMemebers.objects.filter(dialog__in=dialogues).\
        values_list('member_id', flat=True)
    new_interlocutors = User.objects.exclude(pk__in=interlocutors)

    context = {
        'page_title': 'новый диалог',
        'new_interlocutors': new_interlocutors,
    }
    return render(request, 'mainapp/dialog_create.html', context)


def user_dialog_create(request, user_id):
    interlocutor = User.objects.get(pk=user_id)
    dialog = Dialog.objects.create(
        name=interlocutor.username
    )
    DialogMemebers.objects.create(
        dialog=dialog,
        member=request.user,
        role=DialogMemebers.CREATOR
    )
    DialogMemebers.objects.create(
        dialog=dialog,
        # member_id=user_id,
        member=interlocutor,
        role=DialogMemebers.INTERLOCUTOR
    )

    return HttpResponseRedirect(
        reverse('main:dialog_show', kwargs={'dialog_pk': dialog.pk})
    )
