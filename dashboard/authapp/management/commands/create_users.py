from django.core.management.base import BaseCommand

from authapp.models import UserProfile


class Command(BaseCommand):
    help = "Creates default users"

    def handle(self, *args, **options):
        UserProfile.objects.create_superuser('kpk', password='pass')
        UserProfile.objects.create_user('user1', password='pass')
        print('users created')
