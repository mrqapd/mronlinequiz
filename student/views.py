from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from quiz import models as QMODEL
from teacher import models as TMODEL
from mbti import models as MModel
from tatest import models as TModel
from mbti.models import MQuestion as MBTIMQuestion
from tatest.models import TQuestion as TAQuestion
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return render(request, 'quiz/logout.html')
def get_question_model_for_course(course):
    # Implement the logic to determine the question model based on the course
    # For example, if the course name contains 'MBTI', return MBTIQuestion, else return ElseQuestion
    if 'MBTI' in course.course_name:
        return MBTIMQuestion
    elif 'TATEST' in course.course_name:
        return TAQuestion
    # else:
    #     return 0

#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'student/studentsignup.html',context=mydict)

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    courses=QMODEL.Course.objects.all()

    return render(request,'student/student_dashboard.html',{'courses':courses})
    
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    courses=QMODEL.Course.objects.all()

    return render(request,'student/student_exam.html',{'courses':courses})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    question_model = get_question_model_for_course(course)
    print(question_model)
    total_questions=question_model.objects.all().filter(course=course).count()
    questions=question_model.objects.all().filter(course=course)
    total_marks=0
    for q in questions:
        total_marks=total_marks
    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    question_model = get_question_model_for_course(course)
    questions=question_model.objects.all().filter(course=course)
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response


@login_required(login_url='studentlogin')
@user_passes_test(is_student)

#Sabse Badi Dikkat Yahan Hai
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)
        if course.course_name == 'MBTI':
            question_model = get_question_model_for_course(course)
            questions = question_model.objects.all().filter(course=course)
            total_marks = 0

            # Initialize category scores
            category_counters = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

            student = models.Student.objects.get(user_id=request.user.id)
            result = MModel.Result_mbti()

            for i, question  in enumerate(questions, start=1):
            #for i in range(len(questions)):
                selected_ans = request.COOKIES.get(str(i))
                print(selected_ans)

                if i % 4 == 1:
                    # category = 'E' if selected_ans == 'option1' else 'I'
                    if selected_ans == 'Option1':
                        category_counters['E'] += 1
                    elif selected_ans == 'Option2':
                        category_counters['I'] += 1
                elif i % 4 == 2:
                    if selected_ans == 'Option1':
                        category_counters['S'] += 1
                    elif selected_ans == 'Option2':
                        category_counters['N'] += 1
                elif i % 4 == 3:
                    if selected_ans == 'Option1':
                        category_counters['T'] += 1
                    elif selected_ans == 'Option2':
                        category_counters['F'] += 1
                elif i % 4 == 0:
                    if selected_ans == 'Option1':
                        category_counters['J'] += 1
                    elif selected_ans == 'Option2':
                        category_counters['P'] += 1 


                # if selected_ans == 'option2':
                #     # If option2 is selected, choose the opposite category
                #     category = 'I' if category == 'E' else 'E'
                #     category = 'N' if category == 'S' else 'S'
                #     category = 'F' if category == 'T' else 'T'
                #     category = 'P' if category == 'J' else 'J'

                # category_counters[category] += 1  # Increment the counter for the selected category
                total_marks += 1  # Increment the total marks

            # Save the result instance with the total marks and category scores
            result.student = student
            result.exam = course
            result.marks = total_marks

            # Set category counters
            for cat, counter in category_counters.items():
                setattr(result, f'category_{cat}', counter)

            result.save()

            return HttpResponseRedirect('view-result')
        elif course.course_name == 'TATEST':
            question_model = get_question_model_for_course(course)
            questions = question_model.objects.all().filter(course=course)

            type_counters = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}    

            student = models.Student.objects.get(user_id=request.user.id)
            result = TModel.Result_ta()
            total_marks = 0

            for i, question  in enumerate(questions, start=1):
               selected_ans = request.COOKIES.get(str(i))
               print(question.type)
            #    category_key = str(question.category)
               if selected_ans == 'Option1':
                   total_marks += 0
                   type_counters[question.type.pk]+=0
               elif selected_ans == 'Option2':
                   total_marks += 1
                   type_counters[question.type.pk]+=1
               elif selected_ans == 'Option3':
                   total_marks += 2
                   type_counters[question.type.pk]+=2
               elif selected_ans == 'Option4':
                   total_marks += 3
                   type_counters[question.type.pk]+=3
               elif selected_ans == 'Option5':
                   total_marks += 4
                   type_counters[question.type.pk]+=4
            
               print('Value of Category Counter')
               print(type_counters[question.type.pk])
               print(f'After processing Question {i}: category is={question.type.pk}category_counters[question.type.pk]={type_counters[question.type.pk]}')
                   

            result.student = student
            result.exam = course
            result.marks = total_marks
            result.category_I = type_counters[1]
            result.category_II = type_counters[2]
            result.category_III = type_counters[3]
            result.category_IV = type_counters[4]
            result.category_V = type_counters[5]
            result.category_VI = type_counters[6]
            result.save()
            return HttpResponseRedirect('view-result')
               

            

           




@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})
    

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    if course.course_name == 'MBTI':
        mresults= MModel.Result_mbti.objects.all().filter(exam=course).filter(student=student)
        return render(request,'student/check_marks_mbti.html',{'mresults' :mresults})
    elif course.course_name == 'TATEST':
        tresults= TModel.Result_ta.objects.all().filter(exam=course).filter(student=student)
        return render(request,'student/check_marks_tatest.html',{'tresults' :tresults})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})
  
