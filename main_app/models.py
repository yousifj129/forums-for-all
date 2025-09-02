from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin" # value saved in db, value shown to the user
        USER = "user", "User"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        # default=Role.CUSTOMER,
        null=True
    )