import random
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.shortcuts import render
from django.utils.text import slugify
from taggit.managers import TaggableManager
from taggit.models import Tag, TagBase

from startIT_utils.text import translite
from users.models import User



class Question(models.Model):
    ACTIVE = 'активный'
    IN_PROCESSING = 'в процессе'
    RETURNED = 'возвращен'
    ACCEPTED = 'принят'
    DELETED = 'удален'

    STATUS_CHOICES = (
        (ACTIVE, 'активный'),
        (IN_PROCESSING, 'в процессе'),
        (RETURNED, 'возвращен'),
        (ACCEPTED, 'принят'),
        (DELETED, 'удален')
    )
    author = models.ForeignKey(User,on_delete=models.PROTECT,
                               verbose_name='автор', name='author')
    tag = TaggableManager(verbose_name="Тег", related_name='tag')
    question = models.CharField(verbose_name='Вопрос', max_length=500,
                                name='question')
    slag = models.SlugField(verbose_name='Слаг', max_length=500,
                            allow_unicode=True, name='slag')
    answer = RichTextUploadingField(verbose_name='Ответ', name='answer')
    data_created = models.DateField(verbose_name='дата создания',
                                    auto_now_add=True, name="data_created")
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE,
                                verbose_name='Комментарии', name='comment',
                                blank=True, null=True)
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES,
                              default=IN_PROCESSING, max_length=15, blank=True,
                              name='status')
    pro = models.BooleanField(verbose_name='pro подписка', default=False,
                              name='pro')
    is_delete = models.BooleanField(default=False, verbose_name='Удален',
                                    name='is_delete')

    class Meta:
        db_table = 'questions'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question[:25]

    def save(self, *args, **kwargs):
        if not self.slag:
            self.slag = translite(self.question)
        super(Question, self).save(*args, **kwargs)

    @staticmethod
    def get_questions(workout, count):
        all_questions = Question.objects.filter(is_delete=False)
        try:
            question_in_workout = workout.questions.all()
        except ValueError:
            question_in_workout = []
        if count > 1:
            while True:
                question = random.choice(all_questions)
                if question not in question_in_workout:
                    return question.id
                else:
                    continue
        else:
            return 0



class Comment(models.Model):

    ACTIVE = 'активный'
    DELETED_FOR_INSULTING = 'удален за оскорбление'
    DELETE_FOR_VIOLATING_CENSORSHIP = 'удален за нарушение цензуры'

    STATUS_CHOICES = (
        (ACTIVE, 'активный'),
        (DELETED_FOR_INSULTING, 'удален за оскорбление'),
        (DELETE_FOR_VIOLATING_CENSORSHIP, 'удален за нарушение цензуры'),
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, name='user',
                             verbose_name='Пользователь')
    text = models.CharField(max_length=1000, verbose_name='Комментарий',
                            name='text')
    data_created = models.DateField(auto_now_add=True, name='data_created',
                                    verbose_name='Дата создания')
    status = models.CharField(choices=STATUS_CHOICES, default=ACTIVE,
                              max_length=35, verbose_name='Статус',
                              name='status')
    is_delete = models.BooleanField(default=False, verbose_name='Удален',
                                    name='is_delete')
    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.user} + {self.text[:10]}'

