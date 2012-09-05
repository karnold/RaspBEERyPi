from django.core.management.base import BaseCommand, CommandError
from beer import sensors

class Command(BaseCommand):
    help = 'Check the reading of your beer'
    s = sensors.sensors()

    def handle(self, *args, **options):
        (celsius, fahrenheit) = self.s.readTemp()
        print "The temp reading is " + str(celsius) + " celsius, " + str(fahrenheit) + " fahrenheit."
        #gravity = sensors.readGravity() 

        
        
