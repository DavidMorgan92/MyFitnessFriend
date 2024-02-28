from django.shortcuts import render
from allauth.account.decorators import login_required
from .models import FoodDiary, FoodDiaryEntry


@login_required
def index(request):
    context = {
        'breakfast': [],
        'lunch': [],
        'dinner': [],
        'snacks': []
    }

    if request.GET and 'date' in request.GET:
        food_diary = FoodDiary.objects.filter(
            owner__exact=request.user.id,
            date__exact=request.GET['date']).first()

        if food_diary != None:
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
