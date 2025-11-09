from django import forms
from .models import Department,Student,Course
from django.core.exceptions  import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {'student_name':"Name"}
        
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
        
        
def clean_mark(self):
    mark = self.cleaned_data['mark']
    if mark < 0 or mark > 100:
        raise forms.ValidationError("Marks should be between 0 and 100")
    return mark
