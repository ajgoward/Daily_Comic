from django.urls import path
from . import views

urlpatterns = [
    path('', views.see_the_bag, name='see_the_bag'),
]
