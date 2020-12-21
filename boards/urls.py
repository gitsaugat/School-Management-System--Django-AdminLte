from django.urls import path,include
from .views import dashboard , _404
urlpatterns = [
  path('dashboard/' , dashboard , name = "dashboard"),
  path('404/' , _404 , name = "404")
]
