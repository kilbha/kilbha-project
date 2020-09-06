from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionInput(models.Model):
    Question = models.TextField(default='')
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    rand_url = models.TextField(default='')

    def __str__(self):
        return self.Question