from django.core.management.base import BaseCommand, CommandError
from beer import sensors

class Command(BaseCommand):
    help = 'Check the reading of your beer'
    s = sensors.sensors()

    def handle(self, *args, **options):
        (celsius, fahrenheit) = self.s.readTemp()
        ctemp = "%0.2f" % (celsius)
        ftemp = "%0.2f" % (fahrenheit)
        print "The temp reading is " + str(ctemp) + " degrees celsius, " + str(ftemp) + " degrees fahrenheit."
        #gravity = sensors.readGravity() 

        
        
