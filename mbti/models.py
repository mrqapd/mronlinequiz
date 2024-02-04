from django.db import models
from quiz.models import Course
from student.models import Student
class MQuestion(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE, default = 1)
    question = models.CharField(max_length = 600)
    option1 = models.CharField(max_length = 200, null = True)
    option2 = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.question
    
class Result_mbti(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    # Scores for each category
    category_E = models.PositiveIntegerField(default=0)
    category_I = models.PositiveIntegerField(default=0)
    category_S = models.PositiveIntegerField(default=0)
    category_N = models.PositiveIntegerField(default=0)
    category_T = models.PositiveIntegerField(default=0)
    category_F = models.PositiveIntegerField(default=0)
    category_J = models.PositiveIntegerField(default=0)
    category_P = models.PositiveIntegerField(default=0)

