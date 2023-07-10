from django.urls import path
from . import views

app_name = "goldprice"
urlpatterns = [
    path('', views.index, name="index"),
    path('current', views.current_datetime),
    path('new', views.newPrice, name="new"),

]
