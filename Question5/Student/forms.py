from django import forms
from .models import Course,Department,Student
from django.core.exceptions import ValidationError
import re

class CourseForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Course
    
    def clean_semesterNo(self):
        sem = self.cleaned_data.get('semesterNo')
        if sem < 1 or sem > 8:
            raise ValidationError("Semester number must be between 1 and 8.")
        return sem



    
class StudentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Student
    
    def clean_studentID(self):
        sid = self.cleaned_data.get('studentID')
        if not len(sid)==9:
            raise ValidationError("Student ID must be 9 characters (letters/numbers only).")
        return sid
        
        
    def clean_mark(self):
        mark = self.cleaned_data.get('mark')
        if mark < 0 or mark > 100:
            raise ValidationError("Mark must be between 0 and 100.")
        return mark




class DepartmentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Department
        
    def clean_blockNo(self):
        block = self.cleaned_data.get('blockNo')
        if not re.fullmatch(r'[A-Z]', block):
            raise ValidationError("Block number must be a single uppercase letter (A–Z).")
        return block   
        
    def clean_deptID(self):
        dept_id = self.cleaned_data.get('deptID')
        if dept_id % 10 != 0:
            raise ValidationError("Department ID must be a multiple of 10.")
        return dept_id