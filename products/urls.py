from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_stock, name='products'),
    path('<int:product_id>/', views.item_detail, name='item_detail'),
    ]
