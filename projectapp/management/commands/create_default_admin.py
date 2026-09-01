from django.core.management.base import BaseCommand
from decouple import config
from django.contrib.auth.models import User  


class Command(BaseCommand):
    help = "Helps to create the default admin user to handle things"

    admin_username = config("DEFAULT_ADMIN_USERNAME")
    admin_password = config("DEFAULT_ADMIN_PASSWORD")

    def handle(self, *args, **kwargs):
        if not (self.admin_username and self.admin_password):
            self.stdout.write(self.style.ERROR("Default admin username and password are not set in the environment variables."))
            return
        if User.objects.filter(username=self.admin_username).exists():
            self.stdout.write(self.style.ERROR(f"Default admin user '{self.admin_username}' already exists."))
        else:
            admin_user = User.objects.create_superuser(username=str(self.admin_username), password=str(self.admin_password), email=None)
            self.stdout.write(self.style.SUCCESS(f"Default admin user '{admin_user.username}' created successfully."))