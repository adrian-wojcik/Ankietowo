from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from .forms import ChoiceForm, QuestionCreateForm, QuestionForm, QuestionFormUser
from .models import Choice, Question



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(create_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionFormUser
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        question = form.save()
        choices = []
        for i in range(1, 7):
            choice_text = form.cleaned_data.get(f'choice{i}', None)
            if choice_text:
                choice = Choice(question=question, choice_text=choice_text)
                choices.append(choice)
        Choice.objects.bulk_create(choices)
        return redirect('polls:index')

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()


class ChoiceCreate(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'polls/choice_form.html'
    success_url = reverse_lazy('polls:index')
