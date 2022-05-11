from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workouts.api_views import WorkoutModelViewSet, WorkoutQuestionViewSet
from questions.api_views import QuestionModelViewSet, CommentModelViewSet
from users.api_views import UserModelViewSet


router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('questions', QuestionModelViewSet)
router.register('comments_questions', CommentModelViewSet)
router.register('workouts', WorkoutModelViewSet)
router.register('workouts_questions', WorkoutQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]