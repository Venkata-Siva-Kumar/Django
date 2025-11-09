from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.add_student,name="add_student"),
    path('view/',views.view_students,name="view_students"),
    path('update/<int:id>',views.update_student,name="update_student"),
    path('delete/<int:id>',views.delete_student,name="delete_student"),
    path('top/',views.top_students,name="top_students"),
    
]