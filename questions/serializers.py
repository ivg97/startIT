from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Question, Comment


class QuestionModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'author', 'question', 'slag', 'answer', 'data_created',
                  'comment', 'status', 'pro', 'is_delete',]


class CommentModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'data_created', 'status', 'is_delete',]

