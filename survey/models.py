from django.db import models
from user.models import User


class UserSubmit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey_form = models.ForeignKey('SurveyForm', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class SurveyForm(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Type(models.TextChoices):
        TEXT = 'text'
        MULTIPLE_CHOICE = 'multiple_choice'
        CHECKBOX = 'checkbox'

    survey_form = models.ForeignKey(SurveyForm, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    order = models.PositiveIntegerField()
    type = models.CharField(max_length=50, choices=Type.choices)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_submit = models.ForeignKey(UserSubmit, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer to {self.question.title} by {self.user_submit.user.username}"
