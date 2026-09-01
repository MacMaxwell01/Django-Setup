from django.core.management.base import BaseCommand
from decouple import config
from django.contrib.auth.models import User  


class Command(BaseCommand):
    help = "Helps to create the default admin user to handle things"

    def handle(self, *args, **kwargs):
        admin_username = config("DEFAULT_ADMIN_USERNAME", default=None)
        admin_password = config("DEFAULT_ADMIN_PASSWORD", default=None)
        
        if not (admin_username and admin_password):
            self.stdout.write(self.style.ERROR("Default admin username and password are not set in the environment variables."))
            return
        if User.objects.filter(username=admin_username).exists():
            self.stdout.write(self.style.ERROR(f"Default admin user '{admin_username}' already exists."))
        else:
            admin_user = User.objects.create_superuser(admin_username, admin_password)
            self.stdout.write(self.style.SUCCESS(f"Default admin user '{admin_user.username}' created successfully."))