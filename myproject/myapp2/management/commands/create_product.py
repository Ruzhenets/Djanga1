from django.core.management.base import BaseCommand
from myproject.myapp2.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='product', description='12345', price=64_999.99, amount=20)
        product.save()
        self.stdout.write(f'{product}')
