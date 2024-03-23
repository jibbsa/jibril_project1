from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_form, name='order_form'),
    path('data/', views.data_display, name='data_display'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
