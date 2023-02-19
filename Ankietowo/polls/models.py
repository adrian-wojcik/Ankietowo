from django.db import models


class Questionnaire(models.Model):
    """Representation of whole Questionnaire with any questions"""

    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"


class Question(models.Model):
    """Class that representing Questionnaire"""

    question_text = models.CharField(max_length=400)
    create_date = models.DateTimeField(auto_now_add=True)
    reference = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question_text}"


class Option(models.Model):
    """Class representing options to answer on question from Questionnaire"""

    answer = models.CharField(max_length=200)
    reference = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.answer}"
