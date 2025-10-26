from django.shortcuts import render,redirect
from .models import Employee,Department
from .forms import EmployeeForm,DepartmentForm

# Create your views here.

def emp_list(request):
    employees = Employee.objects.all()
    return render(request,'emp_list.html',{'employees':employees})

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm()
    return render(request,'emp_form.html',{'form':form})

def dept_list(request):
    departments = Department.objects.all()
    return render(request,'dept_list.html',{'departments':departments})

def add_dept(request):
    form  = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dept_list')
    
    return render(request,'dept_form.html',{'form':form})
