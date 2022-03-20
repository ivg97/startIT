from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

from questions.models import Question
from workouts.models import Workout, WorkoutQuestion


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('count_questions',)

    def __init__(self, *args, **kwargs):
        super(CreateWorkoutForm, self).__init__(*args , **kwargs)
        self.fields['count_questions'].widget.attrs['value'] = 'number'
        self.fields['count_questions'].widget.attrs['min'] = '2'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_count_questions(self):
        data = self.cleaned_data['count_questions']
        if len(Question.objects.all()) < data:
            raise ValidationError(gettext_lazy(f'Вы не можете выбрать '
                                               f'вопросов, больше чем их '
                                               f'существует. Выберите не более'
                                        f' {len(Question.objects.all())}.'))
        if data == 1:
            raise ValidationError(gettext_lazy(f'Один вопрос, это не серьезно!'
                                               ))
        return data




class AnswerForm(forms.ModelForm):
    class Meta:
        model = WorkoutQuestion
        fields = ('rating',)