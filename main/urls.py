from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
