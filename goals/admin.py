from django.contrib import admin
from .models import MacroGoal


class MacroGoalAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'calories',
        'carbs_grams',
        'fat_grams',
        'protein_grams',
        'sodium_milligrams',
        'sugar_grams',
    )

    ordering = ('owner',)


admin.register(MacroGoal, MacroGoalAdmin)
