from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Parent(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    child_name = models.CharField(max_length=200, help_text="Child's name enrolled in the academy")
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_current_month_payment(self):
        """Get payment record for current month"""
        today = timezone.now()
        payment, created = Payment.objects.get_or_create(
            parent=self,
            month=today.month,
            year=today.year,
            defaults={'amount': 5000}  # Default monthly fee
        )
        return payment
    
    def get_payment_status_for_month(self, month, year):
        """Get payment status for a specific month"""
        try:
            payment = Payment.objects.get(parent=self, month=month, year=year)
            return payment.is_paid
        except Payment.DoesNotExist:
            return False


class Payment(models.Model):
    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]
    
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='payments')
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    year = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=5000.00)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(blank=True, null=True)
    marked_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', '-month']
        unique_together = ['parent', 'month', 'year']
    
    def __str__(self):
        status = "Paid" if self.is_paid else "Pending"
        return f"{self.parent.name} - {self.get_month_display()} {self.year} ({status})"
    
    def save(self, *args, **kwargs):
        if self.is_paid and not self.paid_at:
            self.paid_at = timezone.now()
        elif not self.is_paid:
            self.paid_at = None
            self.marked_by = None
        super().save(*args, **kwargs)
    
    @property
    def month_name(self):
        return self.get_month_display()
