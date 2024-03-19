from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Product(models.Model):
    class Category(models.IntegerChoices):
        EQUIPMENT = 1
        CLOTHING = 2
        OTHER = 3

    name = models.CharField(max_length=255)
    price_pounds = models.DecimalField(max_digits=8, decimal_places=2, validators=[
                                       MinValueValidator(0), MaxValueValidator(999999.99)])
    category = models.IntegerField(choices=Category, default=Category.OTHER)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price_pounds = models.DecimalField(max_digits=8, decimal_places=2, validators=[
                                       MinValueValidator(0), MaxValueValidator(999999.99)])


class Order(models.Model):
    class State(models.IntegerChoices):
        PLACED = 0
        CONFIRMED = 1
        PAID = 2
        DELIVERED = 3
        RECEIVED = 4

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    state = models.IntegerField(choices=State, default=State.PLACED)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(999999.99)])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)])
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(999999.99)])
