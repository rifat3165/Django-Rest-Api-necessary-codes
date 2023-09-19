from django.urls import path
from . import views


urlpatterns = [ 
    path('b/', views.blog, name="blog"),
    path('f/', views.ShowFormData)
]