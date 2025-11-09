from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,Department,Course
from .forms import StudentForm,DepartmentForm,CourseForm
# Create your views here.

def home(request):
    return render(request,'home.html')
    
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})
    

def update_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method=='POST':
        form = StudentForm(request.POST ,instance = student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)
    return render(request,'update_student',{'form':form})
    
    
def delete_student(request,id):
    student = get_object_or_404(Student,id=id)
    student.delete()
    return redirect('view_students')
    

    
def top_students(request,cia_no):
    top = (Student.objects.filter(cia_no=cia_no)).order_by('-mark')[0:3]
    return render(request,'top_students.html',{'top':'top','CIA':cia_no})