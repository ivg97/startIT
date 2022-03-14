from django import forms

from questions.models import Question
from workouts.models import Workout, WorkoutQuestion


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('count_questions',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = WorkoutQuestion
        fields = ('rating',)