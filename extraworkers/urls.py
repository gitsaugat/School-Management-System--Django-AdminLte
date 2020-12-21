from django.urls import path
from .views import create_extra_staff ,  extrastaffs , edit_extra_staff , delete_extra_staff
urlpatterns = [
    path('extraworkers/' , extrastaffs , name = "extraworkers"),
    path('add/extraworker/' , create_extra_staff , name = "addextraworker"),
    path('edit/<int:pk>/extraworker/',edit_extra_staff , name = "editextraworker" ),
    path('delete/<int:pk>/extraworker/',delete_extra_staff , name = "deleteextraworker" )
]
