from django.contrib import admin
from .models import FoodDiary, FoodDiaryEntry


class FoodDiaryAdmin(admin.ModelAdmin):
    pass


class FoodDiaryEntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(FoodDiary, FoodDiaryAdmin)
admin.site.register(FoodDiaryEntry, FoodDiaryEntryAdmin)
