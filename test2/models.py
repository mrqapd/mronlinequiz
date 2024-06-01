from django.db import models
from quiz.models import Course
from student.models import Student

# Create your models here.
class t2Type(models.Model):
    type = models.CharField(max_length = 100)
    def __str__(self):
        return self.type

class T2Question(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default = 1)
    type = models.ForeignKey(t2Type, on_delete = models.CASCADE, default = 1)
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200, default = 'Usually')
    option2 = models.CharField(max_length=200, default = 'Often')
    option3 = models.CharField(max_length=200, default = 'Sometimes')
    option4 = models.CharField(max_length=200, default = 'Occasionally')
    option5 = models.CharField(max_length=200, default = 'Rarely')
    option6 = models.CharField(max_length=200, default = 'Never')   
   
    def __str__(self):
        return self.question
        
class result_t2(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    category_EI = models.PositiveIntegerField(default=0)
    category_WC = models.PositiveIntegerField(default=0)
    category_EA = models.PositiveIntegerField(default=0)
    category_WI = models.PositiveIntegerField(default=0)
    category_WA = models.PositiveIntegerField(default=0)
    category_EC = models.PositiveIntegerField(default=0)
    
