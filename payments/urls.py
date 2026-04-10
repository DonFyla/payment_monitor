from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_status, name='payment_status'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mark-payment/<int:payment_id>/', views.mark_payment, name='mark_payment'),
    path('add-parent/', views.add_parent, name='add_parent'),
    path('edit-parent/<int:parent_id>/', views.edit_parent, name='edit_parent'),
    path('delete-parent/<int:parent_id>/', views.delete_parent, name='delete_parent'),
]
