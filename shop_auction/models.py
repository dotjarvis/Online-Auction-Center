

from django.utils import timezone
from datetime import date, datetime
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class AuctionUser(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Prefer not to say", "Prefer not to say"),
    )
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

