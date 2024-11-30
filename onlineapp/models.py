from django.db import models

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
    level = models.CharField(max_length=20)
    intake = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    entery_requirements= models.CharField(max_length=50)
    duration = models.CharField(max_length=30)
    exam_body = models.CharField(max_length=50)
    mode_of_study = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


