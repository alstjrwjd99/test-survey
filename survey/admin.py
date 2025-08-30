from django.contrib import admin
from .models import UserSubmit, SurveyForm, Question, Choice, Answer


@admin.register(UserSubmit)
class UserSubmitAdmin(admin.ModelAdmin):
    list_display = ('user', 'survey_form', 'created')
    list_filter = ('created',)
    search_fields = ('user__username', 'survey_form__title')


@admin.register(SurveyForm)
class SurveyFormAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'survey_form', 'type', 'order')
    list_filter = ('survey_form', 'type')
    search_fields = ('title',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'is_correct')
    list_filter = ('question',)
    search_fields = ('choice_text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_submit', 'question', 'choice', 'text')
    list_filter = ('user_submit', 'question')
    search_fields = ('text',)
    raw_id_fields = ('user_submit', 'question', 'choice')
