from ckeditor.widgets import CKEditorWidget
from django import forms

from questions.models import Question


class CreateQuestionForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget, label='Ответ')
    class Meta:
        model = Question
        fields = ('tag', 'question', 'answer',)
        labels = {'tag': 'Тег', 'question': 'Вопрос', 'answer': 'Ответ'}

    def __init__(self, *args, **kwargs):
        super(CreateQuestionForm, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs['placeholder'] = 'Введите тег'
        self.fields['question'].widget.attrs['placeholder'] = 'Введите вопрос'
        self.fields['answer'].widget.attrs['placeholder'] = 'Введите ответ'
