from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('onlineapplication/', views.apply, name='apply'),
    path('about/', views.about_us, name='about_us' ),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('courses/', views.courses, name='courses'),
    path('applications/', views.application_list, name='application_list'),
    path('search/', views.search, name='search')
]
