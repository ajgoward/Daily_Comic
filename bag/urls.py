from django.urls import path
from . import views

urlpatterns = [
    path('', views.see_the_bag, name='see_the_bag'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('quickadd/<item_id>', views.quick_add, name='quick_add'),
]
