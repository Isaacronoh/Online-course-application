from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('onlineapplication/', views.apply, name='apply'),
    path('about/', views.about_us, name='about_us' ),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('courses/', views.courses, name='courses'),
    path('applications/', views.application_list, name='application_list'),
    path('search/', views.search, name='search'),
    path('studentregistration/', views.studentregistration, name='studentregistration'),
    path('staffregistration/', views.staffregistration, name='staffregistration'),
    path('studentdashboard/', views.studentdashboard, name='studentdashboard'),
    path('login/', views.student_login, name='studentlogin'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('staffdashboard/', views.staffdashboard, name='staffdashboard'),
    path('finance/', views.finance, name='finance'),
    path('staff/enter-results/', views.staff_enter_results, name='staff_enter_results'),
    path('staff/edit-results/<int:result_id>/', views.staff_edit_results, name='staff_edit_results'),
    path('student/view-results/', views.student_view_results, name='student_view_results'),
]
