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
    image = models.ImageField(null=True)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price_delta_pounds = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(-999999.99), MaxValueValidator(999999.99)])


class Order(models.Model):
    class State(models.IntegerChoices):
        PLACED = 0
        PAID = 1
        OUT_FOR_DELIVERY = 2
        DELIVERED = 3
        RECEIVED = 4

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(choices=State, default=State.PLACED)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(999999.99)])
    order_total = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(999999.99)])
    grand_total = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(999999.99)])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)])
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(999999.99)])


class OrderItemVariant(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(
        ProductVariant, on_delete=models.SET_NULL, null=True)


class FeaturedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.IntegerField()
