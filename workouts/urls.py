from django.urls import path
from workouts import views

app_name = 'workouts'


urlpatterns = [
    path('', views.CreateWorkoutView.as_view(), name='create_question'),
    path('question/', views.AnswerView.as_view(),
         name='create_answer'),

]