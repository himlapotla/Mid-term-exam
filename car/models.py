from django.db import models
from django.contrib.auth.models import User
from brand.models import Brand


# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_image = models.ImageField(upload_to='uploads/')
    car_description = models.TextField()
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    car_quantity = models.PositiveIntegerField()
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username