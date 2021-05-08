from django.db import models

# Create your models here.

class Exam(models.Model):
    """
    Exam is the main/parent model which contain questions
    """
    exam_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500, null=True)


class Options(models.Model):
    """
    model option which contain the all 4 options and correct option, connected to the parent model
    """
    option_id = models.AutoField(primary_key=True)
    option_1 = models.CharField(max_length=200, null=True)
    option_2 = models.CharField(max_length=200, null=True)
    option_3 = models.CharField(max_length=200, null=True)
    option_4 = models.CharField(max_length=200, null=True)
    correct_option = models.CharField(max_length=200, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)

class User(models.Model):
    """
    user model contain the user name and total score connected to the parent model exam
    """
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    total_score = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)

