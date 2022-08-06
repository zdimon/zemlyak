from django.core.management.base import BaseCommand, CommandError
from account.models import UserProfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Delete users')
        UserProfile.objects.all().delete()
    