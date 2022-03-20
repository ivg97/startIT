from django.contrib import admin

from workouts.models import Workout, WorkoutQuestion


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_workout', 'average_score', 'count_questions',
                    'is_delete',)
    list_display_links = ('user',)


@admin.register(WorkoutQuestion)
class WorkoutQuestionAdmin(admin.ModelAdmin):
    list_display = ('workout', 'question', 'rating',)
    list_display_links = ('workout',)
