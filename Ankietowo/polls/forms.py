from django import forms
from .models import Choice, Question


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("choice_text",)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]


class QuestionFormUser(forms.ModelForm):
    choice1 = forms.CharField(max_length=200, label="Odpowiedź 1")
    choice2 = forms.CharField(max_length=200, label="Odpowiedź 2")
    choice3 = forms.CharField(max_length=200, label="Odpowiedź 3", required=False)
    choice4 = forms.CharField(max_length=200, label="Odpowiedź 4", required=False)
    choice5 = forms.CharField(max_length=200, label="Odpowiedź 5", required=False)
    choice6 = forms.CharField(max_length=200, label="Odpowiedź 6", required=False)

    class Meta:
        model = Question
        fields = ["question_text"]


class QuestionCreateForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    choice1 = forms.CharField(max_length=200, label="Odpowiedź 1")
    choice2 = forms.CharField(max_length=200, label="Odpowiedź 2")
    choice3 = forms.CharField(max_length=200, label="Odpowiedź 3", required=False)
    choice4 = forms.CharField(max_length=200, label="Odpowiedź 4", required=False)
    choice5 = forms.CharField(max_length=200, label="Odpowiedź 5", required=False)
    choice6 = forms.CharField(max_length=200, label="Odpowiedź 6", required=False)
