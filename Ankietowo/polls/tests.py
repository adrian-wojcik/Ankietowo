from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice, Questionnaire
import datetime
from django.urls import reverse
from .views import IndexView, DetailView, ResultsView, QuestionCreateView


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(create_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(create_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(create_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionnaireModelTests(TestCase):
    def test_questionnaire_str(self):
        """
        __str__() method of Questionnaire model should return the questionnaire_text field
        """
        questionnaire_text = "Test Questionnaire"
        questionnaire = Questionnaire(questionnaire_text=questionnaire_text)
        self.assertEqual(str(questionnaire), questionnaire_text)


class ChoiceModelTests(TestCase):
    def test_choice_str(self):
        """
        __str__() method of Choice model should return the choice_text field
        """
        choice_text = "Test Choice"
        question = Question(question_text="Test Question")
        choice = Choice(question=question, choice_text=choice_text)
        self.assertEqual(str(choice), choice_text)

    def test_choice_default_votes(self):
        """
        votes field of Choice model should be set to 0 by default
        """
        choice_text = "Test Choice"
        question = Question(question_text="Test Question")
        choice = Choice(question=question, choice_text=choice_text)
        self.assertEqual(choice.votes, 0)





class PollsURLTests(TestCase):
    def setUp(self):
        """
        Create some sample data for the tests
        """
        Question.objects.create(question_text="Test question 1", pub_date='2022-01-01')
        Question.objects.create(question_text="Test question 2", pub_date='2022-01-02')

    def test_index_view(self):
        """
        Test the index view, which should display a list of all questions
        """
        response = self.client.get(reverse('polls:index'))
        self.assertNumQueries(1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question 1")
        self.assertContains(response, "Test question 2")
        self.assertTemplateUsed(response, 'polls/index.html')
        self.assertEqual(len(response.context['latest_question_list']), 2)

    def test_detail_view(self):
        """
        Test the detail view, which should display the details of a single question
        """
        question = Question.objects.get(question_text="Test question 1")
        response = self.client.get(reverse('polls:detail', args=(question.id,)))
        self.assertNumQueries(1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question 1")
        self.assertTemplateUsed(response, 'polls/detail.html')

    def test_results_view(self):
        """
        Test the results view, which should display the results of a single question
        """
        question = Question.objects.get(question_text="Test question 1")
        response = self.client.get(reverse('polls:results', args=(question.id,)))
        self.assertNumQueries(1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question 1")
        self.assertTemplateUsed(response, 'polls/results.html')

    def test_question_create_view(self):
        """
        Test the question create view, which should display a form to create a new question
        """
        response = self.client.get(reverse('polls:question_create'))
        self.assertNumQueries(1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/question_form.html')
