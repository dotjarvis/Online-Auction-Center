from django.db import models

# Create your models here.





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
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class AuctionItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='auction_photos/')

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    activity_time = models.DateTimeField(auto_now_add=True)
