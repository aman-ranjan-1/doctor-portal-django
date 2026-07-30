from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    help = "Create demo admin if it does not exist"

    def handle(self, *args, **kwargs):

        email = "admin@citycare.com"

        password = "Admin@123"

        if User.objects.filter(email=email).exists():

            self.stdout.write(

                self.style.SUCCESS(

                    "Demo admin already exists."

                )

            )

            return

        User.objects.create_superuser(

            username=email,

            email=email,

            password=password,

            first_name="CityCare",

            last_name="Admin",

            is_staff=True,

            is_superuser=True

        )

        self.stdout.write(

            self.style.SUCCESS(

                "Demo admin created successfully."

            )

        )