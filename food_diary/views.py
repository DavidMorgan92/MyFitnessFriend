from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.decorators import login_required
import datetime
from .models import FoodDiary, FoodDiaryEntry
from .forms import AddEntryForm


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

    return render(request, 'food_diary/index.html', context)


@login_required
def delete_entry(request, entry_id):
    return render(request, 'food_diary/index.html')


@login_required
def add_entry(request, date):
    if request.method == 'POST':
        form = AddEntryForm(request.POST)

        if form.is_valid():
            # Save new entry in database

            return redirect(reverse('food_diary_index'))
    else:
        form = AddEntryForm()

    context = {
        'form': form,
        'date': date,
    }

    return render(request, 'food_diary/add_entry.html', context)
