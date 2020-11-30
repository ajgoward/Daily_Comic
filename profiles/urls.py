from django.urls import path
from . import views


urlpatterns = [
    path('', views.theProfile, name='theprofile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),

    ]
