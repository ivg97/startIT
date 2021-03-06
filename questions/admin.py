from django.contrib import admin

from questions.models import Question, Comment


@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('author', 'data_created', 'question', 'status', 'is_delete',)
    list_display_links = ('author',)
    prepopulated_fields = {'slag': ('question',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'data_created', 'status', 'is_delete',)
    list_display_links = ('text',)




