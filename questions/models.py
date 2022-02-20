from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify

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
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT, name='tag',
                            verbose_name='Теги')
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


class Tag(models.Model):
    name = models.CharField(max_length=25, verbose_name='Теги', name='name')
    data_created = models.DateField(auto_now_add=True, name='data_created',
                                    verbose_name='Дата создания')
    is_delete = models.BooleanField(verbose_name='Удален', name='is_delete',
                                    default=False)
    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name