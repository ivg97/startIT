from ckeditor.widgets import CKEditorWidget
from django import forms
from taggit.models import Tag

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
        self.fields['tag'].help_text = 'Список тегов разделенных запятыми'
        self.fields['question'].widget.attrs['placeholder'] = 'Введите вопрос'
        self.fields['answer'].widget.attrs['placeholder'] = 'Введите ответ'


        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        labels = {'name': 'Название',}

    def __init__(self, *args, **kwargs):
        super(CreateTagForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


