from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    create_date = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Question
        fields = ('question_text', 'create_date')
