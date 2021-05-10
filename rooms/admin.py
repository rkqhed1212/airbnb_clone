from django.contrib import admin
from django.utils.html import mark_safe
from .import models


@admin.register(models.RoomType, models.Facilitiy, models.Amentity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):


    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline ,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ('name',"description","country", "city", "address", "price","room_type")}
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

    raw_id_fields = ("host", )

    search_fields = ("=city", "^host__username")
    
    filter_horizontal = (
        "amentities",
        "facilities",
        "house_rule",
    ) 
    
    def count_amenities(self, obj):
        return obj.amentities.count()
    count_amenities.short_description = "Amenity Count"

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"  
        


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    
    list_display = ("__str__", 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}">')

    get_thumbnail.short_description = "Thumbnail"