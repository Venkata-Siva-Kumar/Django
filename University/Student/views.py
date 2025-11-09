from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html')
    
 
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request,'form.html',{'form':form,'title':'Student'})
    
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DepartmentForm()
    return render(request,'form.html',{'form':form,'title':'Department'})
    
    
def add_programme(request):
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProgrammeForm()
    return render(request,'form.html',{'form':form,'title':'Programme'})
    
    
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request,'form.html',{'form':form,'title':'Course'})
    
def add_gradesheet(request):
    if request.method == "POST":
        form = GradeSheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GradeSheetForm()
    return render(request,'form.html',{'form':form,'title':'GradeSheet'})
    
    
def grade_sheet(request):
    context = {}
    if request.method == "POST":
        reg_no = request.POST.get("registerNo")
        cia_no = request.POST.get("cia_no")

        student = get_object_or_404(Student, pk=reg_no)
        grades = GradeSheet.objects.filter(registerNo=student)

        # total, average, and grade
        total_marks = 0
        count = grades.count()
        for g in grades:
            total_marks += g.cia1 + g.cia2 + g.cia3 + g.endsem
        average = total_marks / count if count > 0 else 0
        grade = "PASS" if average >= 50 else "FAIL"

        context.update({
            "student": student,
            "total": total_marks,
            "average": average,
            "grade": grade,
        })

    return render(request, "grade_sheet.html", context)
    
    
    
def ece_students(request):
    students = Student.objects.filter(DeptID__dName__icontains='ECE')
    print("ECE Students:", list(students))
    return render(request,'ece_students.html',{'students':students})