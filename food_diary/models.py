from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class FoodDiary(models.Model):
    class Meta:
        verbose_name_plural = 'Food diaries'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()


class FoodDiaryEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Food diary entries'

    class Meal(models.IntegerChoices):
        BREAKFAST = 1
        LUNCH = 2
        DINNER = 3
        SNACKS = 4

    food_diary = models.ForeignKey(FoodDiary, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    meal = models.IntegerField(choices=Meal, default=Meal.SNACKS)
    calories = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    carbs_grams = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    fat_grams = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    protein_grams = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    sodium_milligrams = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
    sugar_grams = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)])
