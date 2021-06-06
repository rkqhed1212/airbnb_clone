from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid 
from django.conf import settings
from django.shortcuts import reverse
from django.core.mail import send_mail

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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )
    
    first_name = models.CharField(("first name"), max_length=30, blank=True, default="Unnamed User"
    )
    avatar = models.ImageField(upload_to = "avatars", blank = True)
    gender = models.CharField(choices = GENDER_CHOICSES, max_length=10, null = True)
    bio = models.TextField(default = "", blank = True)
    birthday = models.DateField(null = True)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length = 6, null = True,  blank = True, default = LANGUAGE_KOREAN)
    currency = models.CharField(choices = CURRENCY_CHOICES, max_length = 3, null = True,  blank = True,   default = CURRENCY_KRW)
    superhost = models.BooleanField(default = False)

    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
         if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify Airbnb Account",
                f"Verify account, this is your secret: {secret}",
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
            )
            return



