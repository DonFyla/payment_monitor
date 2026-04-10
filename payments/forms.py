from django import forms
from .models import Parent, Payment


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'email', 'phone', 'child_name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Parent\'s full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone number'}),
            'child_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Child\'s full name'}),
            'address': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Address', 'rows': 3}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'is_paid', 'notes']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 2}),
        }
