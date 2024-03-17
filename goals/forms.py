from django import forms


class SetGoalForm(forms.Form):
    calories = forms.IntegerField(required=True, min_value=0, max_value=9999)
    carbs_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    fat_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    protein_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    sodium_milligrams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    sugar_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
