from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from taggit.models import Tag

from questions.forms import CreateQuestionForm, CreateTagForm
from questions.models import Question


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'questions/create_question.html'
    form_class = CreateQuestionForm
    success_url = reverse_lazy('main:index')



    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            return redirect(self.success_url)
        return redirect(self.success_url)

class CreateTagView(CreateView):
    model = Tag
    template_name = 'questions/create_tag.html'
    form_class = CreateTagForm
    success_url = reverse_lazy('main:index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return redirect(self.success_url)