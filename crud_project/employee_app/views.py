from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request,'add_employee.html',{'form':form})
    
def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})
   
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'edit_employee.html', {'form': form})

# Delete
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'confirm_delete.html', {'employee': employee})