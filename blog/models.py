from django.db import models
from django.utils import timezone 
from django_markdown.models import MarkdownField
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	description = models.TextField('Descrição Simples', blank=True)
	text  = MarkdownField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
		ordering = ['-create_date']
