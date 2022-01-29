from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from authapp.models import UserProfile


class Command(BaseCommand):
    help = "Creates auth tokens for users"

    def handle(self, *args, **options):
        cnt = 0
        for user in UserProfile.objects.all():
            token = Token.objects.create(user=user)
            print(user, token.key)
            cnt += 1

        print(f'tokens created: {cnt}')
