from urllib import request
from django.shortcuts import render, redirect
from .models import Slider,Card1,Card2,Card3,Application,Course
from onlineapp.models import Status
from django.contrib import messages
from . serializers import ApplicationSerializer
from rest_framework import viewsets
from django.db.models import Q


# online application
def apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        id_number = request.POST.get('id number')
        postal_address = request.POST.get('adress')
        primary_school = request.POST.get('name-primary')
        primary_grade = request.POST.get('grade-primary')
        primary_year = request.POST.get('Year-primary')
        secondary_school = request.POST.get('name-secondary')
        secondary_grade = request.POST.get('grade-secondary')
        secondary_year = request.POST.get('Year-Secondary')
        course = request.POST.get('course')
        level = request.POST.get('level')
        intake = request.POST.get('intake')
        photo = request.FILES.get('photo')

        application = Application(
            name=name,
            gender=gender,
            email=email,
            phone=phone,
            id_number=id_number,
            postal_address=postal_address,
            primary_school=primary_school,
            primary_grade=primary_grade,
            primary_year=primary_year,
            secondary_school=secondary_school,
            secondary_grade=secondary_grade,
            secondary_year=secondary_year,
            course=course,
            level=level,
            intake=intake,
            photo=photo
        )
        application.save()
        messages.success(request, 'Application has been submitted successfully. Thank you!')

    return render(request, 'onlineapplication.html')

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

def about_us(request):
    return render(request, 'about_us.html')

def stafflogin(request):
    return render(request, 'stafflogin.html')

def studentlogin(request):
    return render(request, 'studentlogin.html')

def courses(request):
    return render(request, 'courses.html')

    
    #home
     
def home(request):
    slider = Slider.objects.all()  
    card1 = Card1.objects.first()
    card2 = Card2.objects.first()
    card3 = Card3.objects.first()
    status = Status.objects.first()  
    if not status:
        context = {
            'attachment': 0,
            'session': 0,
            'graduated': 0,
        }
    else:
        context = {
            'attachment': status.attachment,
            'session': status.session,
            'graduated': status.graduated,
        }
    context['slider']= slider
    context['card1']= card1
    context['card2'] = card2
    context['card3'] = card3
    return render(request, 'home.html', context)

# view application

class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer



def search(request):
    query= request.GET.get('search')
    if query:
        courses = Course.objects.filter(Q(course_name__icontains=query) | Q(code__icontains = query))
        return render(request, 'search.html',{'courses' : courses})
    return render(request, 'courses.html')
