from django.core.management import BaseCommand

from users.models import User, UserRoles


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='sky@pro.ru',
            first_name='moderator',
            last_name='skypro',
            is_staff=True,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MODERATOR
        )
        user.set_password('simba2106')
        user.save()
