from django.shortcuts import render,redirect
from .models import Course,Department,Student
from .forms import CourseForm,DepartmentForm,StudentForm


# Create your views here.

def home(request):
    return render(request,'home.html')
    
    
def add_Student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = StudentForm()
    return render(request,'form.html',{'form':form})
    
    
def add_Department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = DepartmentForm()
    return render(request,'form.html',{'form':form})
    

def add_Course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = CourseForm()
    return render(request,'form.html',{'form':form})
    
    
def search_students(request):
    students = None
    if request.method == 'POST':
        dept_name = request.POST.get('department')
        try:
            department = Department.objects.get(deptName=dept_name)
            students = Student.objects.filter(deptID=department)
        except Department.DoesNotExist:
            students = []
    return render(request, 'search_students.html', {'students': students})
