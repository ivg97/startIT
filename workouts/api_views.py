from rest_framework.viewsets import ModelViewSet
from .models import Workout, WorkoutQuestion
from .serializers import WorkoutModelSerializer, WorkoutQuestionModelSerializer


class WorkoutModelViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutModelSerializer


class WorkoutQuestionViewSet(ModelViewSet):
    queryset = WorkoutQuestion.objects.all()
    serializer_class = WorkoutQuestionModelSerializer

