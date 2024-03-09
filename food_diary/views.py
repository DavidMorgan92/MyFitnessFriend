from django.shortcuts import render, redirect, get_object_or_404
from allauth.account.decorators import login_required
import datetime
from .models import FoodDiary, FoodDiaryEntry
from .forms import AddEntryForm
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
