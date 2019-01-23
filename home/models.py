from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class MyUser(AbstractUser):

    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$',
                                 message="Phone number must be entered in the format: '+88'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)  # validators should be a list

    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-update"]


class Reward(models.Model):
    text = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-update"]