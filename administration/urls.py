from django.urls import path
from .views import create_admin_staff ,adminstaffs  , edit_adminstaff_info , delete_admin_staff
urlpatterns = [
    path('adminstaffs/' , adminstaffs , name = "adminstaffs"),
    path('add/adminstaff/' , create_admin_staff , name = "createadminstaff"),
    path('edit/<int:pk>/adminstaff/',edit_adminstaff_info , name = "editadminstaff" ),
    path('delete/<int:pk>/adminstaff/',delete_admin_staff , name = "deleteadminstaff" )

   
]
