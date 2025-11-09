from django import forms
from .models import Department ,Programme,Student,Course,GradeSheet

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date' : forms.DateInput(attrs={'type':'date'}),
            }
        
class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = "__all__"
        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date' : forms.DateInput(attrs={'type':'date'}),
            }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'DOB': forms.DateInput(attrs={'type':'date'}),
            'join_date' : forms.DateInput(attrs={'type':'date'}),
            }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class GradeSheetForm(forms.ModelForm):
    class Meta:
        model = GradeSheet
        fields = "__all__"        