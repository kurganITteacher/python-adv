from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('dialog/show/<int:dialog_pk>/', mainapp.dialog_show, name='dialog_show'),
    path('dialog/create/', mainapp.dialog_create, name='dialog_create'),
    path('user/dialog/create/<int:user_id>/', mainapp.user_dialog_create,
         name='user_dialog_create'),
    path('user/dialog/delete/<int:pk>/', mainapp.dialog_delete,
         name='dialog_delete'),

    path('dialog/member/<int:sender_pk>/message/create/',
         mainapp.DialogMessageCreate.as_view(),
         name='dialog_message_create'),

    path('user/dialog/update/<int:dialog_pk>/',
         mainapp.dialog_show_update,
         name='dialog_show_update'),
]
