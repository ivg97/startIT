import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from questions.models import Question
from workouts.forms import CreateWorkoutForm, AnswerForm
from workouts.models import Workout, WorkoutQuestion


class CreateWorkoutView(CreateView):
    model = Workout
    template_name =  'workouts/create_workout.html'
    form_class = CreateWorkoutForm
    success_url = reverse_lazy('workouts:create_question')
    redirect_url = reverse_lazy('workouts:create_answer')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect(self.redirect_url)
        return redirect(self.success_url)


class AnswerView(CreateView):
    model = WorkoutQuestion
    template_name = 'workouts/create_answer.html'
    form_class = AnswerForm
    success_url = reverse_lazy('workouts:create_answer')
    check = []

    def get_context_data(self, *args, **kwargs):
        context = super(AnswerView, self).get_context_data(*args, **kwargs)
        questions = Question.objects.all()
        while True:
            id = random.randint(0, len(questions) - 1)
            if id not in self.check:
                self.check.append(id)
                break
            else:
                if len(self.check) == len(questions):
                    break
                continue
        context['question'] = questions[id]
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            # new_form.workout = self.get_queryset()
            # new_form.question = self.get_queryset()
            new_form.save()


