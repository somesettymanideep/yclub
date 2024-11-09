from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('dashboard/', views.dashtwo, name='dashboard'),
    path('payouts/', views.payouts, name='payouts'),
    path('datatables/', views.datatables, name='datatables'),
    path('loans/', views.loans, name='loans'),
    path('invoices/', views.invoices, name='invoices'),
    path('profile/', views.profile, name='profile'),
    path('contactbook/', views.contactbook, name='contactbook'),
    path('cards/', views.cards, name='cards'),
    path('collect/', views.collect, name='collect'),
    path('utility_payments/', views.utility_payments, name='utility_payments'),
    path('merchant_device/', views.merchant_device, name='merchant_device'),
    path('settlements/', views.settlements, name='settlements'),
    path('statements/', views.statements, name='statements'),
    path('contactbook/', views.contactbook, name='contactbook'),
    path('addinvoice/', views.addinvoice, name='addinvoice'),
    path('device/', views.device, name='device'),

]
