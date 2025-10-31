from django.urls import path
from . import views
urlpatterns = [
    path('insert/',views.insert_plant,name = "insert_plant"),
    path('update/<int:id>',views.update_plant,name = "update_plant"),
    path('show/',views.show_plants,name = "show_plants"),
]
