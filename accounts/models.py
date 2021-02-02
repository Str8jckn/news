from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User 

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    create_user = models.ForeignKey(
        User, related_name = '%(class)s_requests_created',
        on_delete = models.CASCADE
    )

    