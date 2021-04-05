from django.contrib.auth.models import User
from django.db import models


class Dialog(models.Model):
    created = models.DateTimeField(verbose_name='отправлено',
                                   auto_now_add=True,
                                   db_index=True)
    name = models.CharField(verbose_name='имя', max_length=64, blank=True)

    def __str__(self):
        result = f'{self.created.strftime("%Y.%m.%d %H:%M")}'
        if self.name:
            result += f' ({self.name})'
        return result

    class Meta:
        verbose_name = 'диалог'
        verbose_name_plural = 'диалоги'
        ordering = ['-created']


class DialogMemebers(models.Model):
    CREATOR = '0'
    INTERLOCUTOR = '1'

    ROLE_CHOICES = (
        (CREATOR, 'создатель'),
        (INTERLOCUTOR, 'собеседник'),
    )

    dialog = models.ForeignKey(Dialog,
                               verbose_name='диалог',
                               on_delete=models.CASCADE,
                               related_name="members")
    member = models.ForeignKey(User,
                               verbose_name='участник диалога',
                               on_delete=models.CASCADE,
                               related_name="dialogs")
    role = models.CharField(verbose_name='роль',
                            choices=ROLE_CHOICES,
                            # default=CREATOR,
                            max_length=64,
                            db_index=True)

    class Meta:
        ordering = ['dialog', '-role', 'member']


class Message(models.Model):
    sender = models.ForeignKey(DialogMemebers,
                               verbose_name='отправитель',
                               on_delete=models.CASCADE)
    text = models.TextField(verbose_name='сообщение')
    read = models.BooleanField(verbose_name='прочитано', default=False)
    created = models.DateTimeField(verbose_name='отправлено',
                                   auto_now_add=True,
                                   db_index=True)

    def __str__(self):
        return f'{self.sender} ({self.created}):\n\t{self.text[:35]}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        # ordering = ['sender', '-created']
        ordering = ['-created']
