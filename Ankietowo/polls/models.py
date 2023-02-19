from django.db import models
from django.db.models import DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField, Model, TextField



class questionnaire(models.Model):
    reference = IntegerField(primary_key="ref")
    question_text = models.CharField(max_length=400)
    publicy_date = models.DateTimeField('Data dodania ankiety')
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)


class user(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, primary_key="email")
    date_of_birth = models.DateField('Data Urodzenia')

