from django.core.management.base import BaseCommand, CommandError
from beer import sensors
from beer.models import Batch, Reading
import datetime 

class Command(BaseCommand):
    help = 'Check the reading of your beer'
    s = sensors.sensors()

    def handle(self, *args, **options):
        date = datetime.datetime.now() 
        temperature = self.s.readTemp()

        # temporary debug code until we add gravity sensor
        gravity = 0
        #gravity = self.s.readGravity() 

        # save the reading to the database
        reading = Reading(date=date, temperature=temperature, gravity=0)
        reading.save()

        print "The temp reading is " + str(temperature) + " celsius, " + str(self.s.tempFahrenheit(temperature)) + " fahrenheit."
