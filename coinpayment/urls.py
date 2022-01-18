from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('success/', views.success_payment, name='success-payment'),
    path('cancel/', views.cancel_payment, name='cancel-payment'),
    path('webhook/', views.coinbase_webhook)
]