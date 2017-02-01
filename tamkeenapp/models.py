"""
Definition of models.
"""
import django.core.management

from django.db import models

# Create your models here.
class Workshop(models.Model):
        title=models.CharField( max_length=250)
        notes=models.TextField(blank=True, null=True)
        start_date=models.DateTimeField()
        hours=models.IntegerField(default=0)
        instructor=models.CharField(max_length=200)
        place=models.CharField(max_length=250)
        #books=models.OneToOneField(
        course = models.ForeignKey(
        'Course',
        models.SET_NULL,
        blank=True,
        null=True,
        )

        def __str__(self):           
            return self.title

class Subscriber(models.Model):
        name=models.CharField(max_length=200)
        email=models.EmailField()
        def __str__(self):           
            return self.name
        #publishesAt=models.DateField()
        #author=models.ForeignKey(Author)
         #if here foreign key field 

class Course(models.Model):
    course_name=models.CharField(max_length=200) 
    start_date =models.DateTimeField( blank=True, null=True)
    price=models.FloatField()
    avaliablity=models.BooleanField()
    hours=models.IntegerField(default=0)
    description=models.TextField()
    topics_covered=models.TextField()
    notes=models.CharField(max_length=500)
    has_certificate=models.BooleanField(default='false')
    has_workshop=models.BooleanField()
    def topics_covered_as_list(self):
        if self.topics_covered:
            return self.topics_covered.split(';')
        else:
            return ''
    def __str__(self):           
        return self.course_name
    def short_description(self):
        return self.description[0:130]+"..."
         

class Certificate(models.Model):
    name=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    usecase_title=models.CharField(max_length=200)
    usecases=models.TextField()
    course= models.ForeignKey(
        'Course',
        models.SET_NULL,
        blank=True,
        null=True,
        )
    def usecases_as_list(self):
        if self.usecases:
            return self.usecases.split(',')
        else:
            return ''

    def __str__(self):           
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    enquiry=models.TextField()
    def __str__(self):           
        return self.name