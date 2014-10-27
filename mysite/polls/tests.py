from django.test import TestCase
from django.utils import timezone

from polls.models import Question

# Create your tests here.
class QuestionMethodTests(TestCase):
	

	def test_published_recently_with_future_question():
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_data=time)
		self.assertEqual(future_question.published_recently(), False)
		