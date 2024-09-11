from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.sign, name='sign'),
    path('log/', views.loginn, name='log'),
    path('pro/', views.profile, name='pro'),
    path('out/', views.logoutt, name='out'),
    path('edit/', views.edit_profile, name='edit'),
    path('/<int:id>/', views.buy_car, name='buy_car'),
]

