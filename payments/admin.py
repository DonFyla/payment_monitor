from django.contrib import admin
from .models import Parent, Payment


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'child_name', 'created_at']
    search_fields = ['name', 'email', 'child_name']
    list_filter = ['created_at']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['parent', 'month', 'year', 'amount', 'is_paid', 'paid_at', 'marked_by']
    list_filter = ['is_paid', 'month', 'year', 'paid_at']
    search_fields = ['parent__name', 'notes']
    date_hierarchy = 'paid_at'
    list_editable = ['is_paid', 'amount']
    
    def save_model(self, request, obj, form, change):
        if obj.is_paid and not obj.marked_by:
            obj.marked_by = request.user
        super().save_model(request, obj, form, change)
