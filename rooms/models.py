from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
# Create your models here.

class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    

    class Meta:
        verbose_name_plural = "Room Type"
        ordering = ['created']  

class Amentity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"

class Facilitiy(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilties"

class HouseRule(AbstractItem):
    
    class Meta:
        verbose_name_plural = "House Rule"

class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to = "room_photos")
    room = models.ForeignKey("Room", related_name = "photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):
    
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guest = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=True)
    host = models.ForeignKey("users.User",  related_name = "rooms", on_delete = models.CASCADE)
    room_type = models.ForeignKey("RoomType", related_name = "rooms", on_delete = models.SET_NULL, null = True)
    amentities = models.ManyToManyField("Amentity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facilitiy", related_name="rooms", blank=True)
    house_rule = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)


    def __str__(self):
        return self.name


    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings  = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)
            