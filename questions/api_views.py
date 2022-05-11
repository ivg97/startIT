from rest_framework.viewsets import ModelViewSet
from .models import Question, Comment
from .serializers import QuestionModelSerializer, CommentModelSerializer



class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer