from django.urls import path
from questions import views

app_name = 'questions'


urlpatterns = [
    path('', views.CreateQuestionView.as_view(), name='create_question'),

]