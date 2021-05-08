from django.db import models

# Create your models here.

#creating table to restore data from student
class Studentdetails(models.Model): 
    studentid = models.IntegerField()
    firstname = models.CharField(max_length = 500)
    lastname = models.CharField(max_length = 500)
    studentmajor = models.CharField(max_length = 500)
    studentyear = models.CharField(max_length = 500)
    studentgpa = models.DecimalField(max_digits = 3, decimal_places = 2, default =  None)
    
    
class Coursedetails(models.Model):
    courseid = models.IntegerField() #primary_key = true in the () to make it primary
    coursetitle = models.CharField(max_length = 500)
    coursename = models.TextField()
    coursesection = models.IntegerField()
    coursedepartment = models.TextField()
    courseinstructor = models.TextField()
    
class CommentData(models.Model):
    emailid = models.CharField(max_length = 500)
    commentdata = models.TextField()
    
    
class Studentenrollment(models.Model):
    sname = models.CharField(max_length = 500)
    course = models.CharField(max_length = 500)
    