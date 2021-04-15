from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "rooms"

def room_detail(request):

    render(request, "rooms/details.html")