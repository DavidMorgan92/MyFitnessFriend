from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class MacroGoal(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    calories = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    carbs_grams = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    fat_grams = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    protein_grams = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    sodium_milligrams = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    sugar_grams = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
