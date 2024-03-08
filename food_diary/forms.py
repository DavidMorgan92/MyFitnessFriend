from django import forms
from .models import FoodDiaryEntry


class AddEntryForm(forms.Form):
    name = forms.CharField(required=True, max_length=255)
    meal = forms.TypedChoiceField(required=True, coerce=int, choices=FoodDiaryEntry.Meal)
    calories = forms.IntegerField(required=True, min_value=0, max_value=9999)
    carbs_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    fat_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    protein_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    sodium_milligrams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    sugar_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
