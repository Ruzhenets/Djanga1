from django.core.management.base import BaseCommand
from myproject.myapp2.models import Client

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Alex', email='alex@em.em', phone='+19991112233',
                            address='NY, 5th st, bld 5, apt 25')
        cclient.save()
        self.stdout.write(f'{client}')


