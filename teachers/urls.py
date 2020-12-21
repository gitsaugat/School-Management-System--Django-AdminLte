from django.urls import path
from .views import create_teacher , teachers , edit_teachers_info , delete_teacher
urlpatterns = [
    path('teachers/' , teachers , name = "teachers"),
    path('add/teacher/' , create_teacher , name = "addteacher"),
    path('edit/<int:pk>/teacher/',edit_teachers_info , name = "editteacherinfo" ),
    path('delete/<int:pk>/teacher/',delete_teacher , name = "deleteteacher" )

   
]
