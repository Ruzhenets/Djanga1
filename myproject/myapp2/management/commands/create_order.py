from django.core.management.base import BaseCommand
from myproject.myapp2.models import Order

class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        order = Order(product='product', client='12345', total_price=333333, order_date="24.04.2024")
        order.save()
        self.stdout.write(f'{order}')