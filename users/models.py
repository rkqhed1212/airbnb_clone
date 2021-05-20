from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser): 

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICSES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female")
    )
    
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "KOREAN")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )

    avatar = models.ImageField(upload_to = "avatars", blank = True)
    gender = models.CharField(choices = GENDER_CHOICSES, max_length=10, null = True)
    bio = models.TextField(default = "", blank = True)
    birthday = models.DateField(null = True)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length = 6, null = True,  blank = True, default = LANGUAGE_KOREAN)
    currency = models.CharField(choices = CURRENCY_CHOICES, max_length = 3, null = True,  blank = True,   default = CURRENCY_KRW)
    superhost = models.BooleanField(default = False)
