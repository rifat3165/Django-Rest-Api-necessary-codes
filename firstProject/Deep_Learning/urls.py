from django.urls import path
from . import views


urlpatterns = [ 
    path('d/', views.deep_learning),
    path('reg/', views.registration)
]