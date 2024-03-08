from .models import FoodDiaryEntry


def meal_ids(_):
    """Context processor that provides named values for food diary entry meal times"""

    return {
        'MEAL_BREAKFAST': FoodDiaryEntry.Meal.BREAKFAST,
        'MEAL_LUNCH': FoodDiaryEntry.Meal.LUNCH,
        'MEAL_DINNER': FoodDiaryEntry.Meal.DINNER,
        'MEAL_SNACKS': FoodDiaryEntry.Meal.SNACKS,
    }
