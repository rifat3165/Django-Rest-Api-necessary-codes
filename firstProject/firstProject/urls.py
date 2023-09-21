"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drapi import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ml/', include('Machine_learning.urls')),
    path('deep/', include('Deep_Learning.urls')),
    path('blog/', include('blog1.urls')),
    path('data/', include('Data_Analysis.urls')),
    path('about/', include('About_Us.urls')),
    # path('aiinfo/', views.aiquest_info),              #show info in site(comment)
    # path('aiinfo/<int:pk>', views.aiquest_ins),        #show info in site by id(comment)
    # path('aicreate/', views.aiquest_create, name='aicreate'),         #function based view url(comment)
    # path('aicreate/<int:pk>', views.aiquest_create, name='aicreate'),     #function based view url(comment)
    # path('aicreate/', views.AiquestCreate.as_view(), name='aicreate'),         #class based view url(comment)
    # path('aicreate/<int:pk>', views.AiquestCreate.as_view(), name='aicreate'),       #class based view url(comment
    path('ailist/', views.Aiquestlist.as_view(), name='ailist'),
    path('aicreate-mdl/', views.AiquestCreateModel.as_view(), name='aicreate-mdl'),
    path('airetrieve/<int:pk>/', views.AiquestRetrieve.as_view()),
    path('aiupdate/<int:pk>/', views.AiquestUpdate.as_view()),
    path('aidestroy/<int:pk>/', views.AiquestDelete.as_view()),

]
