from django.core.management.base import BaseCommand
from rooms.models import Amentity


class Command(BaseCommand):

    help = "this command tell me that he loves me"
    
    def handle(self, *args, **options):
        amenities = [
            'Air conditioning',
            'Alarm Clock',
            'Balcony',
            'Bathroom',
            'Bathtub',
            'Bed Linen',
            'Boating',
            'Cable TV',
            'Indoor Pool',
            'Ironing Board',
            'Microwave',
            'Outdoor Pool',
            'Outdoor Tennis',
            'Oven',
            'Queen size bed',
            'Restaurant',
            'Shopping Mall',
            'Shower',
            'Smoke detectors',
            'Sofa',
            'Stereo',
            'Swimming pool',
            'Toilet',
            'Towels',
            'TV'
        ]
        
        for a in amenities:
            Amentity.objects.create(name = a )
        self.stdout.write(self.style.SUCCESS("Amenities created!"))