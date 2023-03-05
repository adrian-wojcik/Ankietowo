import datetime

from django.db import models
from django.utils import timezone


class Questionnaire(models.Model):
    questionnaire_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.questionnaire_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_date <= now

    was_published_recently.admin_order_field = "create_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class DoesNotExist:
        pass
