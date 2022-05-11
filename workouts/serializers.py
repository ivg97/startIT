from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Workout, WorkoutQuestion


class WorkoutModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'questions', 'count_questions', 'data_workout',
                  'average_score', 'is_delete',]


class WorkoutQuestionModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = WorkoutQuestion
        fields = ['id', 'workout', 'question', 'rating']
