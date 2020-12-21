
from django.urls import path
from .views import students , add_student , edit_student , edit_student_info , delete_student
urlpatterns = [
    path('students/' , students , name = "students"),
    path('add/students/' , add_student , name = "addstudents"),
    path('edit/students/' , edit_student , name = "editstudent"),
    path('edit/<int:pk>/student/' , edit_student_info , name = "editstudentinfo"),
    path('delete/<int:pk>/student/' , delete_student, name = "deletestudents" )
]
