from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    attachment = models.IntegerField(default=0)
    session = models.IntegerField(default=0)
    graduated = models.IntegerField(default=0)



    def __str__(self):
        return str(self.session)

# slider section

class Slider(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    slider_image = models.ImageField(upload_to='slides/')


    def __str__(self):
        return self.tittle

#    announcement section

class Card1(models.Model):
    tittle1 = models.CharField(max_length=50)
    description1 = models.CharField(max_length=250)

    def __str__(self):
        return self.tittle1
    

class Card2(models.Model):
    tittle2 = models.CharField(max_length=50)
    description2 = models.CharField(max_length=250)

    def __str__(self):
        return self.tittle2
    

class Card3(models.Model):
    tittle3 = models.CharField(max_length=50)
    description3 = models.CharField(max_length=250)

    def __str__(self):
        return self.tittle3
    

# application form

class Application(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    id_number = models.CharField(max_length=20)
    postal_address = models.CharField(max_length=100)
    primary_school = models.CharField(max_length=100, blank=True, null=True)
    primary_grade = models.CharField(max_length=10, blank=True, null=True)
    primary_year = models.CharField(max_length=4, blank=True, null=True)
    secondary_school = models.CharField(max_length=100, blank=True, null=True)
    secondary_grade = models.CharField(max_length=10, blank=True, null=True)
    secondary_year = models.CharField(max_length=4, blank=True, null=True)
    course = models.CharField(max_length=50)
    year_of_admission = models.CharField(max_length=4, blank=True, null=True)
    level = models.CharField(max_length=20)
    intake = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    # courses model
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    entery_requirements= models.CharField(max_length=50)
    duration = models.CharField(max_length=30)
    exam_body = models.CharField(max_length=50)
    mode_of_study = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


# staff registration model.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.staff_number})"



# student registration

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    adm_number = models.CharField(max_length=20, unique=True)
    id_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.full_name

# finance model

class Finance(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    total_billed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property
    def balance(self):
        return self.total_billed - self.total_paid

    def __str__(self):
        return f"Finance for {self.student.username}: Billed {self.total_billed}, Paid {self.total_paid}"



# academics button

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    subject = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.subject} - {self.marks} for {self.student.username}"