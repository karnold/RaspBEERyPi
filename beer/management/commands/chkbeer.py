from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Check the reading of your beer'

    def handle(self, *args, **options):
        #do some stuff here
	print 'TODO'
