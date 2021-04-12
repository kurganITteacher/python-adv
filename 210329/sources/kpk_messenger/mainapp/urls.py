from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('dialog/show/<int:dialog_pk>/', mainapp.dialog_show, name='dialog_show'),
    path('dialog/create/', mainapp.dialog_create, name='dialog_create'),
]
