from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from allauth.account.decorators import login_required
from .models import MacroGoal
from .forms import SetGoalForm, GoalWizardForm


@login_required
def index(request):
    goals = MacroGoal.objects.get_or_create(owner=request.user)[0]

    form = SetGoalForm(initial={
        'calories': goals.calories,
        'carbs_grams': goals.carbs_grams,
        'fat_grams': goals.fat_grams,
        'protein_grams': goals.protein_grams,
        'sodium_milligrams': goals.sodium_milligrams,
        'sugar_grams': goals.sugar_grams,
    })

    if request.method == 'POST':
        form = SetGoalForm(request.POST)

        if form.is_valid():
            goals.calories = form.cleaned_data['calories']
            goals.carbs_grams = form.cleaned_data['carbs_grams']
            goals.fat_grams = form.cleaned_data['fat_grams']
            goals.protein_grams = form.cleaned_data['protein_grams']
            goals.sodium_milligrams = form.cleaned_data['sodium_milligrams']
            goals.sugar_grams = form.cleaned_data['sugar_grams']
            goals.save()

    context = {
        'form': form,
        'goal_wizard_form': GoalWizardForm(),
    }

    return render(request, 'goals/index.html', context)


@login_required
@require_http_methods(['POST'])
def wizard(request):
    form = GoalWizardForm(request.POST)

    if form.is_valid():
        goals = MacroGoal.objects.get_or_create(owner=request.user)[0]

        rmr = 10 * form.cleaned_data['weight_kg'] + 6.25 * form.cleaned_data['height_cm'] - 5 * form.cleaned_data['age']
        rmr -= 161 if form.cleaned_data['gender'] == 1 else -5

        match form.cleaned_data['activity_level']:
            case 0:
                rmr *= 1.2

            case 1:
                rmr *= 1.375

            case 2:
                rmr *= 1.55

            case 3:
                rmr *= 1.725

            case 4:
                rmr *= 1.9

        match form.cleaned_data['goal']:
            case 0:
                goals.calories = int(rmr - 500)

            case 1:
                goals.calories = int(rmr)

            case 2:
                goals.calories = int(rmr + 500)

        weight_pounds = form.cleaned_data['weight_kg'] * 2.2

        goals.protein_grams = int(weight_pounds * 1.5)

        protein_calories = goals.protein_grams * 4
        remaining_calories = goals.calories - protein_calories
        carbs_calories = remaining_calories / 2
        fat_calories = remaining_calories / 2

        goals.carbs_grams = int(carbs_calories / 4) - 25
        goals.fat_grams = int(fat_calories / 9)
        goals.sodium_milligrams = 1500
        goals.sugar_grams = 25
        goals.save()

    return redirect(reverse('goals_index'))
