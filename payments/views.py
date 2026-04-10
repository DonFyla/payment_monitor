from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Parent, Payment
from .forms import PaymentForm, ParentForm


def payment_status(request):
    """
    Public view showing payment status of all parents.
    Accessible by anyone - no login required.
    """
    # Get current month and year
    today = timezone.now()
    current_month = request.GET.get('month', today.month)
    current_year = request.GET.get('year', today.year)
    
    try:
        current_month = int(current_month)
        current_year = int(current_year)
    except (ValueError, TypeError):
        current_month = today.month
        current_year = today.year
    
    # Get all parents with their payment status for selected month
    parents = Parent.objects.all()
    parent_payments = []
    
    total_parents = parents.count()
    paid_count = 0
    pending_count = 0
    
    for parent in parents:
        payment, created = Payment.objects.get_or_create(
            parent=parent,
            month=current_month,
            year=current_year,
            defaults={'amount': 5000}
        )
        
        if payment.is_paid:
            paid_count += 1
        else:
            pending_count += 1
            
        parent_payments.append({
            'parent': parent,
            'payment': payment
        })
    
    context = {
        'parent_payments': parent_payments,
        'current_month': current_month,
        'current_year': current_year,
        'month_name': Payment.MONTH_CHOICES[current_month - 1][1],
        'month_choices': Payment.MONTH_CHOICES,
        'total_parents': total_parents,
        'paid_count': paid_count,
        'pending_count': pending_count,
    }
    return render(request, 'payments/payment_status.html', context)


@staff_member_required
def admin_dashboard(request):
    """
    Admin dashboard for managing payments.
    Only accessible by staff/admin users.
    """
    today = timezone.now()
    current_month = request.GET.get('month', today.month)
    current_year = request.GET.get('year', today.year)
    
    try:
        current_month = int(current_month)
        current_year = int(current_year)
    except (ValueError, TypeError):
        current_month = today.month
        current_year = today.year
    
    parents = Parent.objects.all()
    parent_payments = []
    
    total_parents = parents.count()
    paid_count = 0
    pending_count = 0
    total_collected = 0
    
    for parent in parents:
        payment, created = Payment.objects.get_or_create(
            parent=parent,
            month=current_month,
            year=current_year,
            defaults={'amount': 5000}
        )
        
        if payment.is_paid:
            paid_count += 1
            total_collected += payment.amount
        else:
            pending_count += 1
            
        parent_payments.append({
            'parent': parent,
            'payment': payment
        })
    
    context = {
        'parent_payments': parent_payments,
        'current_month': current_month,
        'current_year': current_year,
        'month_name': Payment.MONTH_CHOICES[current_month - 1][1],
        'month_choices': Payment.MONTH_CHOICES,
        'total_parents': total_parents,
        'paid_count': paid_count,
        'pending_count': pending_count,
        'total_collected': total_collected,
    }
    return render(request, 'payments/admin_dashboard.html', context)


@staff_member_required
def mark_payment(request, payment_id):
    """
    Toggle payment status for a parent.
    Only accessible by staff/admin users.
    """
    payment = get_object_or_404(Payment, id=payment_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'mark_paid':
            payment.is_paid = True
            payment.marked_by = request.user
            payment.save()
            messages.success(request, f"Payment marked as paid for {payment.parent.name}")
        elif action == 'mark_unpaid':
            payment.is_paid = False
            payment.marked_by = None
            payment.paid_at = None
            payment.save()
            messages.success(request, f"Payment marked as pending for {payment.parent.name}")
        
        # Redirect back to the referring page
        next_url = request.POST.get('next', 'admin_dashboard')
        return redirect(next_url)
    
    return redirect('admin_dashboard')


@staff_member_required
def add_parent(request):
    """
    Add a new parent to the system.
    """
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Parent added successfully!')
            return redirect('admin_dashboard')
    else:
        form = ParentForm()
    
    return render(request, 'payments/add_parent.html', {'form': form})


@staff_member_required
def edit_parent(request, parent_id):
    """
    Edit an existing parent's information.
    """
    parent = get_object_or_404(Parent, id=parent_id)
    
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            messages.success(request, 'Parent information updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = ParentForm(instance=parent)
    
    return render(request, 'payments/edit_parent.html', {'form': form, 'parent': parent})


@staff_member_required
def delete_parent(request, parent_id):
    """
    Delete a parent from the system.
    """
    parent = get_object_or_404(Parent, id=parent_id)
    
    if request.method == 'POST':
        parent.delete()
        messages.success(request, 'Parent deleted successfully!')
        return redirect('admin_dashboard')
    
    return render(request, 'payments/delete_parent.html', {'parent': parent})
