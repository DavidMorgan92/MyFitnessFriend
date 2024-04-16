from django import forms


class SetGoalForm(forms.Form):
    calories = forms.IntegerField(required=True, min_value=0, max_value=9999)
    carbs_grams = forms.IntegerField(
        required=True, min_value=0, max_value=9999)
    fat_grams = forms.IntegerField(required=True, min_value=0, max_value=9999)
    protein_grams = forms.IntegerField(
        required=True, min_value=0, max_value=9999)
    sodium_milligrams = forms.IntegerField(
        required=True, min_value=0, max_value=9999)
    sugar_grams = forms.IntegerField(
        required=True, min_value=0, max_value=9999)


class GoalWizardForm(forms.Form):
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )

    ACTIVITY_CHOICES = (
        (0, 'Sedentary (little or no exercise)'),
        (1, 'Lightly active (light exercise/sports 1-3 days per week)'),
        (2, 'Moderately active (moderate exercise/sports 3-5 days per week)'),
        (3, 'Very active (hard exercise/sports 6-7 days per week)'),
        (4, 'Extra active (very hard exercise/sports and physical job)'),
    )

    GOAL_CHOICES = (
        (0, 'To lose weight'),
        (1, 'To maintain weight'),
        (2, 'To gain weight'),
    )

    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    weight_kg = forms.FloatField(
        required=True, min_value=0, max_value=1000)
    height_cm = forms.FloatField(
        required=True, min_value=0, max_value=1000)
    age = forms.IntegerField(required=True, min_value=0, max_value=100)
    activity_level = forms.ChoiceField(required=True, choices=ACTIVITY_CHOICES)
    goal = forms.ChoiceField(required=True, choices=GOAL_CHOICES)
