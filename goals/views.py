from django.shortcuts import render
from allauth.account.decorators import login_required
from .models import MacroGoal
from .forms import SetGoalForm


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
    }

    return render(request, 'goals/index.html', context)
