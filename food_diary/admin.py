from django.contrib import admin
from .models import FoodDiary, FoodDiaryEntry


class FoodDiaryAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'owner',
    )

    ordering = ('-date', 'owner')


class FoodDiaryEntryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'food_diary',
        'meal',
        'calories',
        'carbs_grams',
        'fat_grams',
        'protein_grams',
        'sodium_milligrams',
        'sugar_grams',
    )

    ordering = ('food_diary', 'name')


admin.site.register(FoodDiary, FoodDiaryAdmin)
admin.site.register(FoodDiaryEntry, FoodDiaryEntryAdmin)
