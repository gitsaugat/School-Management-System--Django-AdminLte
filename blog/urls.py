from django.urls import path,include
from .views import (
    create_academic_post , 
    create_general_post , 
    edit_academic_post,
    edit_general_post,
    delete_general_post,
    general_posts,
    delete_academic_post,
    academic_posts
)
urlpatterns = [
    path('create/academic/post' , create_academic_post , name = "createacademicpost"),
    path('create/general/post' , create_general_post , name = "creategeneralpost"),
    path('update/academic/post/<int:pk>' , edit_academic_post , name = "updateacademicpost"),
    path('update/general/post/<int:pk>' , edit_general_post , name = "editgeneralpost"),
    path('general/posts/all/' , general_posts , name = "allgeneralposts" ),
    path('delete/general/post/<int:pk>' ,delete_general_post , name = "deletegeneralpost" ),
    path('academic/posts/all/' , academic_posts , name = "allacademicposts" ),
    path('delete/general/post/<int:pk>' ,delete_academic_post , name = "deleteacademicpost" )
]
