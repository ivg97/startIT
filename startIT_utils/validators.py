from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

from questions.models import Question


def validate_question_count(value):
    if value > len(Question.objects.all()):
        raise ValidationError(gettext_lazy(f'Вы не можете выбрать вопросов, '
                                           f'больше чем их существует. '
                                           f'Выберите не более '
                                           f'{len(Question.objects.all())}.'))