import random 
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "create many users"
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type = int , help = "how many time used "
        )
    
    

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            review_models.Review, 
            number , 
            {
                "accuray": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "room":lambda x: random.choice(rooms),
                "user":lambda x: random.choice(users),
            })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS('working well'))