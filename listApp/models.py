from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Todo(models.Model):
	text = models.CharField(max_length=160)
	deadline = models.DateTimeField(blank=True, null=True)
	progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

	def create(self):
		self.save()

	def __str__(self):
		return self.text
