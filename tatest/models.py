from django.db import models
from quiz.models import Course
from student.models import Student


class Type(models.Model):
    type = models.CharField(max_length = 100)
    def __str__(self):
        return self.type

class TQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default = 1)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=1)
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200, default = 'Almost never')
    option1_marks = models.IntegerField(default=0)
    option2 = models.CharField(max_length=200, default = 'Rarely')
    option2_marks = models.IntegerField(default=1)
    option3 = models.CharField(max_length=200, default = 'Sometimes')
    option3_marks = models.IntegerField(default=2)
    option4 = models.CharField(max_length=200, default = 'Frequently')
    option4_marks = models.IntegerField(default=3)
    option5 = models.CharField(max_length=200, default = 'Very Frequently')
    option5_marks = models.IntegerField(default=4)

    def __str__(self):
        return self.question

class Result_ta(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    category_I = models.PositiveIntegerField(default=0)
    category_II = models.PositiveIntegerField(default=0)
    category_III = models.PositiveIntegerField(default=0)
    category_IV = models.PositiveIntegerField(default=0)
    category_V = models.PositiveIntegerField(default=0)
    category_VI = models.PositiveIntegerField(default=0)


