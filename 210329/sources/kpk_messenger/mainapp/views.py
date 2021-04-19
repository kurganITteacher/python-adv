from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from mainapp.forms import DialogMessageForm
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
    sender = dialog.get_sender(request.user.pk)

    context = {
        'page_title': 'диалог',
        'dialog': dialog,
        'sender': sender,
    }

    return render(request, 'mainapp/dialog_show.html', context)


def dialog_create(request):
    dialogues = request.user.dialogs.select_related('dialog').all(). \
        values_list('dialog_id', flat=True)
    interlocutors = DialogMemebers.objects.filter(dialog__in=dialogues). \
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


# CBV
def dialog_delete(request, pk):
    # instance = Dialog.objects.filter(pk=pk).first()
    instance = get_object_or_404(Dialog, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('main:index'))


# def dialog_message_create(request):
class DialogMessageCreate(CreateView):
    model = Message
    form_class = DialogMessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        sender_pk = self.request.resolver_match.kwargs['sender_pk']
        # print(context)
        # print(form.fields['sender'].initial)
        # print(dir(form.fields['sender']))
        # print(sender_pk)
        # print(form.initial)
        # form.fields['sender'].initial = sender_pk
        form.initial['sender'] = sender_pk

        return context

    def get_success_url(self):
        # print(self.object.sender.dialog_id)
        # return reverse('main:index')
        return reverse(
            'main:dialog_show',
            kwargs={'dialog_pk': self.object.sender.dialog_id}
        )
