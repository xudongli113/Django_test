import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.question_text

	def published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	published_recently.admin_order_field = 'pub_date'
	published_recently.boolean = True
	published_recently.short_description = 'Published recently?'

	question_text = models.CharField(max_length=200)
	pub_data = models.DateTimeField('date published')
	
class Choice(models.Model):
	def __str__(self):
		return self.choice_text

	quesion = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes=models.IntegerField(default=0)


	
