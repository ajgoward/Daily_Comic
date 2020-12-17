from django.urls import path
from . import views


urlpatterns = [
    path('', views.subscription, name='subs'),
    path('makesub/', views.make_subscription, name='makesub'),
    ]
