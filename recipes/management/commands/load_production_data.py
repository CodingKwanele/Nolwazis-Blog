from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load data to production database'

    def handle(self, *args, **options):
        self.stdout.write('Loading data to production...')
        
        try:
            call_command('loaddata', 'data.json')
            self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))