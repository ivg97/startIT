import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.views.generic.base import View, TemplateView

from questions.models import Question
from workouts.forms import CreateWorkoutForm, AnswerForm
from workouts.models import Workout, WorkoutQuestion


class CreateWorkoutView(CreateView):
    model = Workout
    template_name =  'workouts/create_workout.html'
    form_class = CreateWorkoutForm
    success_url = reverse_lazy('workouts:create_question')
    redirect_url = reverse_lazy('workouts:create_answer')

    def get_context_data(self, **kwargs):
        context = super(CreateWorkoutView, self).get_context_data(**kwargs)
        context['all_questions'] = len(Question.objects.filter(
            is_delete=False))
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST or None)
        if form.is_valid():
            count_questions = form.cleaned_data.get('count_questions')
            new_form = form.save(commit=False)
            new_form.user = request.user
            workout = new_form
            if Workout.check_workout():
                return redirect(reverse_lazy('workouts:today'))
            question_id = Question.get_questions(workout, count_questions)
            if count_questions == 0 or question_id == 0:
                return redirect(reverse_lazy('workouts:result', kwargs={
                    'workout_id': workout.id,
                }))
            new_form.save()

            return redirect(reverse_lazy('workouts:create_answer', kwargs={
                'workout_id': workout.id,
                'question_id': question_id,
            'count': count_questions}))
        else:
            try:
                messages.error(request, form.errors['count_questions'][0])
            except:
                pass
            return redirect(self.success_url)



class AnswerView(CreateView):
    model = WorkoutQuestion
    template_name = 'workouts/create_answer.html'
    form_class = AnswerForm

    def get_context_data(self, *args, **kwargs):
        context = super(AnswerView, self).get_context_data(*args, **kwargs)
        context['question'] = Question.objects.get(
            id=self.kwargs['question_id'])
        context['workout_id'] = self.kwargs['workout_id']
        context['count'] = self.kwargs['count']
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            print('answer', kwargs)
            new_form.workout = Workout.objects.get(id=kwargs['workout_id'])
            new_form.question = Question.objects.get(id=kwargs['question_id'])
            new_form.save()
            workout = Workout.objects.get(id=kwargs['workout_id'])
            count = kwargs['count']
            question_id = Question.get_questions(workout, count)
            if count == 0 or question_id == 0:
                return redirect(reverse_lazy('workouts:result', kwargs={
                    'workout_id': workout.id,
                }))

            return redirect(reverse_lazy('workouts:create_answer', kwargs={
                'workout_id': kwargs['workout_id'],
                'question_id': question_id,
            'count': count - 1 }))
            # return redirect(reverse_lazy('workouts:today'))


class ListResultView(TemplateView):
    template_name = 'workouts/result_workout.html'
    model = Workout

    def get_context_data(self, **kwargs):
        context = super(ListResultView, self).get_context_data(**kwargs)
        workout = Workout.objects.get(id=kwargs['workout_id'])
        Workout.calculate_average_score(workout)
        context['workout'] = workout
        return context


class TodayWorkoutView(TemplateView):
    template_name = 'workouts/today_workout.html'


class AllWorkoutView(TemplateView):
    model = Workout
    template_name = 'workouts/all.html'

    def get_context_data(self, **kwargs):
        context = super(AllWorkoutView, self).get_context_data(**kwargs)
        context['workouts'] = Workout.objects.filter(user=self.request.user)
        return context


class DetailWorkoutView(DetailView):
    model = Workout
    template_name = 'workouts/workout_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailWorkoutView, self).get_context_data(**kwargs)
        workout_questions = WorkoutQuestion.objects.filter(
            workout_id=kwargs['object'].id)
        context['workout_questions'] = workout_questions
        return context