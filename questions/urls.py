from django.urls import path
from questions import views

app_name = 'questions'


urlpatterns = [
    path('', views.CreateQuestionView.as_view(), name='create_question'),
    path('create_tag/', views.CreateTagView.as_view(), name='create_tag'),

]