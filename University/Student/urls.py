from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('student/',views.add_student,name = 'add_student'),
    path('department/',views.add_department,name = 'add_department'),
    path('programme/',views.add_programme,name = 'add_programme'),
    path('course/',views.add_course,name = 'add_course'),
    path('gradesheet/',views.add_gradesheet,name = 'add_gradesheet'),
    path("grades/", views.grade_sheet, name="grade_sheet"),
    path('ece/',views.ece_students,name = 'ece_students'),
]
