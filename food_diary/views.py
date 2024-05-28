from django.shortcuts import render, redirect, get_object_or_404
from allauth.account.decorators import login_required
import datetime
from .models import FoodDiary, FoodDiaryEntry
from .forms import AddEntryForm
from goals.models import MacroGoal
from url_tools import reverse_with_params


@login_required
def index(request):
    # Load diary for the given date or today if none is given
    date = datetime.datetime.strptime(
        request.GET['date'], '%Y-%m-%d') if request.GET and 'date' in request.GET else datetime.date.today()
    
    # By default use empty arrays for the day's diary entries
    context = {
        'date': date,
        'breakfast': [],
        'lunch': [],
        'dinner': [],
        'snacks': [],
        'goal': request.user.macrogoal,
    }

    # Get the food diary for the requesting user with the chosen date
    food_diary = FoodDiary.objects.filter(
        owner__exact=request.user.id,
        date__exact=date).first()

    # Populate the arrays by filtering the diary entries by their meal time
    if food_diary is not None:
        context['breakfast'] = list(food_diary.fooddiaryentry_set.filter(
            meal__exact=FoodDiaryEntry.Meal.BREAKFAST))
        context['lunch'] = list(food_diary.fooddiaryentry_set.filter(
            meal__exact=FoodDiaryEntry.Meal.LUNCH))
        context['dinner'] = list(food_diary.fooddiaryentry_set.filter(
            meal__exact=FoodDiaryEntry.Meal.DINNER))
        context['snacks'] = list(food_diary.fooddiaryentry_set.filter(
            meal__exact=FoodDiaryEntry.Meal.SNACKS))
        
    # TODO The below logic is unpleasant; need to improve its concision; there's probably a way to do it with comprehensions
    breakfast_values = [(e.calories, e.carbs_grams, e.fat_grams, e.protein_grams, e.sodium_milligrams, e.sugar_grams) for e in context['breakfast']]
    breakfast_values.append((0, 0, 0, 0, 0, 0))
    breakfast_totals_t = [sum(x) for x in zip(*breakfast_values)]

    lunch_values = [(e.calories, e.carbs_grams, e.fat_grams, e.protein_grams, e.sodium_milligrams, e.sugar_grams) for e in context['lunch']]
    lunch_values.append((0, 0, 0, 0, 0, 0))
    lunch_totals_t = [sum(x) for x in zip(*lunch_values)]

    dinner_values = [(e.calories, e.carbs_grams, e.fat_grams, e.protein_grams, e.sodium_milligrams, e.sugar_grams) for e in context['dinner']]
    dinner_values.append((0, 0, 0, 0, 0, 0))
    dinner_totals_t = [sum(x) for x in zip(*dinner_values)]

    snacks_values = [(e.calories, e.carbs_grams, e.fat_grams, e.protein_grams, e.sodium_milligrams, e.sugar_grams) for e in context['snacks']]
    snacks_values.append((0, 0, 0, 0, 0, 0))
    snacks_totals_t = [sum(x) for x in zip(*snacks_values)]

    breakfast_totals = {
        'calories': breakfast_totals_t[0],
        'carbs_grams': breakfast_totals_t[1],
        'fat_grams': breakfast_totals_t[2],
        'protein_grams': breakfast_totals_t[3],
        'sodium_milligrams': breakfast_totals_t[4],
        'sugar_grams': breakfast_totals_t[5],
    }

    lunch_totals = {
        'calories': lunch_totals_t[0],
        'carbs_grams': lunch_totals_t[1],
        'fat_grams': lunch_totals_t[2],
        'protein_grams': lunch_totals_t[3],
        'sodium_milligrams': lunch_totals_t[4],
        'sugar_grams': lunch_totals_t[5],
    }

    dinner_totals = {
        'calories': dinner_totals_t[0],
        'carbs_grams': dinner_totals_t[1],
        'fat_grams': dinner_totals_t[2],
        'protein_grams': dinner_totals_t[3],
        'sodium_milligrams': dinner_totals_t[4],
        'sugar_grams': dinner_totals_t[5],
    }

    snacks_totals = {
        'calories': snacks_totals_t[0],
        'carbs_grams': snacks_totals_t[1],
        'fat_grams': snacks_totals_t[2],
        'protein_grams': snacks_totals_t[3],
        'sodium_milligrams': snacks_totals_t[4],
        'sugar_grams': snacks_totals_t[5],
    }

    day_totals = {
        'calories': breakfast_totals['calories'] + lunch_totals['calories'] + dinner_totals['calories'] + snacks_totals['calories'],
        'carbs_grams': breakfast_totals['carbs_grams'] + lunch_totals['carbs_grams'] + dinner_totals['carbs_grams'] + snacks_totals['carbs_grams'],
        'fat_grams': breakfast_totals['fat_grams'] + lunch_totals['fat_grams'] + dinner_totals['fat_grams'] + snacks_totals['fat_grams'],
        'protein_grams': breakfast_totals['protein_grams'] + lunch_totals['protein_grams'] + dinner_totals['protein_grams'] + snacks_totals['protein_grams'],
        'sodium_milligrams': breakfast_totals['sodium_milligrams'] + lunch_totals['sodium_milligrams'] + dinner_totals['sodium_milligrams'] + snacks_totals['sodium_milligrams'],
        'sugar_grams': breakfast_totals['sugar_grams'] + lunch_totals['sugar_grams'] + dinner_totals['sugar_grams'] + snacks_totals['sugar_grams'],
    }

    context['totals'] = {
        'breakfast': breakfast_totals,
        'lunch': lunch_totals,
        'dinner': dinner_totals,
        'snacks': snacks_totals,
        'day': day_totals,
    }

    context['remaining'] = {
        'calories': request.user.macrogoal.calories - day_totals['calories'],
        'carbs_grams': request.user.macrogoal.carbs_grams - day_totals['carbs_grams'],
        'fat_grams': request.user.macrogoal.fat_grams - day_totals['fat_grams'],
        'protein_grams': request.user.macrogoal.protein_grams - day_totals['protein_grams'],
        'sodium_milligrams': request.user.macrogoal.sodium_milligrams - day_totals['sodium_milligrams'],
        'sugar_grams': request.user.macrogoal.sugar_grams - day_totals['sugar_grams'],
    }

    return render(request, 'food_diary/index.html', context)


@login_required
def delete_entry(request, date, entry_id):
    food_diary = get_object_or_404(FoodDiary, owner=request.user, date=date)
    entry = get_object_or_404(FoodDiaryEntry, food_diary=food_diary, pk=entry_id)
    entry.delete()

    return redirect(reverse_with_params('food_diary_index', get={'date': date}))


@login_required
def add_entry(request, date):
    if request.method == 'POST':
        # Load diary for date given
        food_diary = FoodDiary.objects.get_or_create(
            owner=request.user,
            date=date)[0]

        form = AddEntryForm(request.POST)

        if form.is_valid():
            # Save new entry in database
            entry = FoodDiaryEntry(food_diary=food_diary, **form.cleaned_data)
            entry.save()

            return redirect(reverse_with_params('food_diary_index', get={'date': date}))
    else:
        initial = {
            'meal': request.GET['meal'] if request.GET and 'meal' in request.GET else None
        }

        form = AddEntryForm(initial=initial)

    context = {
        'form': form,
        'date': date,
    }

    return render(request, 'food_diary/add_entry.html', context)
