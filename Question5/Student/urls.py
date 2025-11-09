from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_Student/',views.add_Student,name='add_Student'),
    path('add_Course/',views.add_Course,name='add_Course'),
    path('add_Department/',views.add_Department,name='add_Department'),
    path('search_students/', views.search_students, name='search_students'),
    
]
