from django.core.management.base import BaseCommand
from payments.models import Parent, Payment
from django.utils import timezone


class Command(BaseCommand):
    help = 'Creates sample parents and payments for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Sample parents data
        parents_data = [
            {
                'name': 'John Smith',
                'email': 'john.smith@example.com',
                'phone': '08012345678',
                'child_name': 'Michael Smith',
            },
            {
                'name': 'Sarah Johnson',
                'email': 'sarah.j@example.com',
                'phone': '08023456789',
                'child_name': 'Emily Johnson',
            },
            {
                'name': 'David Williams',
                'email': 'david.w@example.com',
                'phone': '08034567890',
                'child_name': 'James Williams',
            },
            {
                'name': 'Mary Brown',
                'email': 'mary.brown@example.com',
                'phone': '08045678901',
                'child_name': 'Sophia Brown',
            },
            {
                'name': 'Robert Jones',
                'email': 'robert.j@example.com',
                'phone': '08056789012',
                'child_name': 'Daniel Jones',
            },
        ]
        
        # Create parents
        for data in parents_data:
            parent, created = Parent.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created parent: {parent.name}'))
            else:
                self.stdout.write(f'Parent already exists: {parent.name}')
        
        # Create payments for current month
        today = timezone.now()
        parents = Parent.objects.all()
        
        for parent in parents:
            payment, created = Payment.objects.get_or_create(
                parent=parent,
                month=today.month,
                year=today.year,
                defaults={'amount': 5000.00}
            )
            if created:
                self.stdout.write(f'Created payment for {parent.name} - {today.strftime("%B %Y")}')
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
