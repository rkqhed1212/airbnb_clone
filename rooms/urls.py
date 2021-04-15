from django.urls import path 
from . import view

app_name = "rooms"
urlpatterns =[path("1", views.room_detail, name="detail")]