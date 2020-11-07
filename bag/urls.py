from django.urls import path
from . import views

urlpatterns = [
    path('', views.see_the_basket, name='see_the_basket'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('quickadd/<item_id>', views.quick_add, name='quick_add'),
    path('adjust/<item_id>/', views.adjust_basket, name='adjust_basket'),
    path(
        'remove/<item_id>/',
        views.remove_from_basket,
        name='remove_from_basket'),
]
