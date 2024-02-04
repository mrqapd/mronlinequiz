from django.db import models

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name
   
    

class Result(models.Model):
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
