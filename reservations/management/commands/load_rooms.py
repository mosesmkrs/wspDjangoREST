from django.core.management.base import BaseCommand
from reservations.models import RoomType

class Command(BaseCommand):
    help = 'Load initial room types'

    def handle(self, *args, **options):
        RoomType.objects.get_or_create(
            name="Sea View",
            description="Luxurious room with ocean view",
            price_per_night=60000,
            capacity=2
        )
        RoomType.objects.get_or_create(
            name="Party Favor",
            description="Large room for groups and parties",
            price_per_night=80000,
            capacity=4
        )
        self.stdout.write(self.style.SUCCESS('Successfully loaded room types'))