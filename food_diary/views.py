from django.shortcuts import render
from allauth.account.decorators import login_required
from .models import FoodDiary, FoodDiaryEntry


@login_required
def index(request):
    food_diary_query = FoodDiary.objects.filter(owner__exact=request.user.id)

    context = {
        'breakfast': [],
        'lunch': [],
        'dinner': [],
        'snacks': []
    }

    if request.GET:
        if 'date' in request.GET:
            food_diary_query = food_diary_query.filter(
                date__exact=request.GET['date'])
            food_diary = food_diary_query.first()

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
