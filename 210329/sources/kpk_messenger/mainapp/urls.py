from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index),
    path('dialog/<int:dialog_pk>/', mainapp.show_dialogue, name='show_dialogue'),
]
