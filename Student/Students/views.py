from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import StaffLogin,Departments,Courses,CompletedCourses,Creditss,Staff,Student
from .forms import StudentLoginForm,StudentForm,CreditsForm

def home(request):
    return render(request,'accounts/login.html')
def login(request):
    if request.method=='POST':
        username=int(request.POST.get('username'))
        password=request.POST.get('password')
        print(username)
        print(password)
        
        if (str(username)[0])!='6':
            student = Student.objects.get(user_id=int(username))
            context={"student_name":student.name,"student_id":student.user_id}
            if int(username)==(student.user_id) and password==student.password:
                    return render(request,'accounts/students.html',context)
            else:
                return HttpResponse("Invalid login credentials")
        else:
            print(username)
            Login=StaffLogin.objects.get(user_id=int(username))
            staff=Staff.objects.get(user_id=int(username))
            context={"staff_name":staff.staff_name,"staff_id":staff.staff_id}
            
            if int(username)==(Login.user_id) and password==Login.password:
                    return render(request,'accounts/staff.html',context)
            else:
                return HttpResponse("Invalid login credentials")
            
def logout(request):
    return render(request,'accounts/login.html')
def profile(request,pk):
    student = Student.objects.get(user_id=pk)
    completed_courses = CompletedCourses.objects.filter(student=student)
    context={"student_profile":student,"Completed_courses":completed_courses}
    return render(request,'accounts/profile.html',context)
def Acedemic(request,pk):
    student = Student.objects.get(user_id=pk)
    courses_info = Creditss.objects.filter(student_id=student.student_id ).values(
    'course__course_name','credit_acquired')
    context = {
        'courses_info': courses_info
    }
    return render(request, 'accounts/adedmic.html', context)
from django.db import connection
from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def createstudent(request, pk):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                # Your SQL cursor logic here
                cursor.execute(
                    "INSERT INTO Students_Student(student_id, name, user_id, department_id, password) VALUES (%s, %s, %s, %s, %s)",
                    [
                        form.cleaned_data['student_id'],
                        form.cleaned_data['name'],
                        form.cleaned_data['user_id'],
                        form.cleaned_data['department'].department_id,
                        form.cleaned_data['password'],
                    ]
                )

            # Continue with the rest of your logic
            staff = Staff.objects.get(staff_id=int(pk))
            context = {"staff_name": staff.staff_name, "staff_id": staff.staff_id}
            return render(request, 'accounts/staff.html', context)
    else:
        form = StudentForm()
    return render(request, 'accounts/create.html', {'form': form, 'pk': pk})

def addcourses(request,pk):
    if request.method=='POST':
        form = CreditsForm(request.POST)
        if form.is_valid():
                form.save()
                staff=Staff.objects.get(staff_id=int(pk))
                context={"staff_name":staff.staff_name,"staff_id":staff.staff_id}
                return render(request,'accounts/staff.html',context)
    else:
        form = CreditsForm()
    return render(request, 'accounts/addcourses.html', {'form': form,"pk":pk})
def go_back(request,pk):
        staff=Staff.objects.get(user_id=int(p_k))
        context={"staff_name":staff.staff_name,"student_id":staff.staff_id}
        return render(request,'accounts/staff.html',context)
def students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, 'accounts/allstudent.html', context)

# Create your views here.
