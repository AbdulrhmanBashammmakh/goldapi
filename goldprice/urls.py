
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cur', views.current_datetime),
]