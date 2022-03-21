import datetime
from collections import Counter

from django.db import models

from questions.models import Question
from users.models import User


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, name='user',
                             verbose_name='Пользователь')
    questions = models.ManyToManyField(Question,
                                       through='WorkoutQuestion',
                                       name='questions',
                                       verbose_name='Вопросы')
    count_questions = models.DecimalField(decimal_places=0, max_digits=2,
                                          default=0, name='count_questions',
                                          verbose_name='Количество вопросов')
    data_workout = models.DateField(auto_now_add=True, name='data_workout',
                                    verbose_name='Дата тренировки')
    average_score = models.DecimalField(decimal_places=1, name='average_score',
                                        verbose_name='Средний балл тренировки',
                                        max_digits=3, default=0)
    is_delete = models.BooleanField(verbose_name='Удалена', name='is_delete',
                                    default=False)

    class Meta:
        db_table = 'workouts'
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return f'{self.user} - {self.data_workout} = {self.average_score}'

    @staticmethod
    def check_workout():
        if len(Workout.objects.filter(data_workout=datetime.date.today())) >= 1:
            return False
        return False

    @staticmethod
    def calculate_average_score(workout):
        questions = WorkoutQuestion.objects.filter(workout=workout)
        summ = sum([i.rating for i in questions])
        count = len(questions)
        workout.average_score = round(summ / count, 1)
        workout.save()





class WorkoutQuestion(models.Model):
    RATING_CHOICES = (
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        # (0, 0),
    )

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE,
                                name='workout', verbose_name='Тренировка')
    question = models.ForeignKey(Question, on_delete=models.PROTECT,
                                 name='question', verbose_name='Вопросы')
    rating = models.DecimalField(choices=RATING_CHOICES, max_digits=1,
                                 name='rating', verbose_name='Оценка',
                                 decimal_places=0, default=2)
    class Meta:
        db_table = 'workout_questions'
        verbose_name = 'Вопрос тренировки'
        verbose_name_plural = 'Вопросы тренировки'

    def __str__(self):
        return f'{self.question} = {self.rating}'

