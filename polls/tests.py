from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.object.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        """
        If no questions exist, an appropriate message should be displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        # print("Response: %s" % response)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_no_question(self):
        """
        If questions exist, no defaulted message should appear
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No polls are available.")
        # self.assertQuerysetEqual(response.context['latest_question_list'], [])
