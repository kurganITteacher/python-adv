from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from mainapp.models import Dialog


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def show_dialogue(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    print(dialog)

    return render(request, 'mainapp/index.html')

