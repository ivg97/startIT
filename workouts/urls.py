from django.urls import path
from workouts import views

app_name = 'workouts'


urlpatterns = [
    path('', views.CreateWorkoutView.as_view(), name='create_question'),
    path('result/<int:workout_id>', views.ListResultView.as_view(), name='result'),
    path('today_workout/', views.TodayWorkoutView.as_view(), name='today'),
    path('question/<int:workout_id>/<int:question_id>/<int:count>/',
         views.AnswerView.as_view(), name='create_answer'),

]