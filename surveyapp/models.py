
from django.db import models


class Survey(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100, default="Python")
    option2 = models.CharField(max_length=100, default="Java")
    option3 = models.CharField(max_length=100, default="C")
    option4 = models.CharField(max_length=100, default="Javascript")

    def __str__(self):
        return self.question


class Response(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="unknown@example.com")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=100, default="")
    rating = models.IntegerField(default=0)
    feedback = models.TextField(default="")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
