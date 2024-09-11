from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_car, name='show_car'),
    path('<int:id>', views.vd, name='vd'),
    path('<str:nm>', views.car_brand, name='car_by_brand'),
]

