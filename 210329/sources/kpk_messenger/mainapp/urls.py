from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('dialog/<int:dialog_pk>/', mainapp.show_dialog, name='show_dialog'),
]
