from django.shortcuts import render
from .models import FoodDiary, FoodDiaryEntry


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
            food_diary_query = food_diary_query.filter(date__exact=request.GET['date'])
            food_diary = food_diary_query.first()

            if food_diary != None:
                context['breakfast'] = list(food_diary.fooddiaryentry_set.filter(meal__exact=FoodDiaryEntry.Meal.BREAKFAST))
                context['lunch'] = list(food_diary.fooddiaryentry_set.filter(meal__exact=FoodDiaryEntry.Meal.LUNCH))
                context['dinner'] = list(food_diary.fooddiaryentry_set.filter(meal__exact=FoodDiaryEntry.Meal.DINNER))
                context['snacks'] = list(food_diary.fooddiaryentry_set.filter(meal__exact=FoodDiaryEntry.Meal.SNACKS))

    return render(request, 'my_profile/index.html', context)

def delete_food_diary_entry(request, entry_id):
    return render(request, 'my_profile/index.html')
