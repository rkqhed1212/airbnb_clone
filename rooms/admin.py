from django.contrib import admin
from .import models


@admin.register(models.RoomType, models.Facilitiy, models.Amentity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):


    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):


    fieldsets = (
        (
            "Basic Info",
            {"fields": ('name',"description","country","address", "price")}
        ),(
            "Time",
            {"fields": ("check_in","check_out", "instant_book")}
        ),
        (
            "Spaces", 
            {"fields": ("guest","beds","baths","bedrooms")}
        ),
        (
            "More About the Space", 
            {
                "classes": ("collapse",),
                "fields": ("amentities","facilities","house_rule")
            }
        ),
        (
            "Last Details", 
            {"fields": ("host",)}
        )
    ) 

    

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost", 
        "room_type",
        "amentities",
        "facilities",
        "house_rule",
        "city", 
        "country",
        )

    search_fields = ("=city", "^host__username")
    
    filter_horizontal = (
        "amentities",
        "facilities",
        "house_rule",
    ) 
    
    def count_amenities(self, obj):
        return obj.amentities.count()

    def count_photos(self, obj):
        return obj.photos.count()
        


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass