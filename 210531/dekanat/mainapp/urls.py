from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('teach/group/create/', mainapp.teach_group_create, name='teach_group_create'),
    # path('teach/group/detail/<int:pk>/', mainapp.teach_group_detail, name='teach_group_detail'),
    # path('teach/group/update/<int:pk>/', mainapp.teach_group_update, name='teach_group_update'),
    # path('teach/group/delete/<int:pk>/', mainapp.teach_group_delete, name='teach_group_delete'),
    #
    # path('student/create/', mainapp.student_create, name='student_create'),
    # path('student/detail/<int:pk>/', mainapp.student_detail, name='student_detail'),
    # path('student/update/<int:pk>/', mainapp.student_update, name='student_update'),
    # path('student/delete/<int:pk>/', mainapp.student_delete, name='student_delete'),
]
