from django.urls import path
from . import views


urlpatterns = [ 
    path('a/', views.about_us, name="about"),
    path('t/', views.teacher_info, name="teacher")
]