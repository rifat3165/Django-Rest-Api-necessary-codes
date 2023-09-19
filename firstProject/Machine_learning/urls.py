from django.urls import path
from . import views


urlpatterns = [ 
    path('machine/', views.machine_learning),
    path('dtree/', views.dtree),
    path('knn/', views.k_nearest),
    path('random/', views.random),

]