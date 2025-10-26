from django.urls import path
from . import views

urlpatterns = [
    path('employees/',views.emp_list,name = "emp_list" ),
    path('employees/add/',views.add_emp,name = "add_emp" ),
    path('departments/',views.dept_list,name = "dept_list" ),
    path('departments/add/',views.add_dept,name = "add_dept" ),
]
