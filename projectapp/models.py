from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f"Title:{self.name}, Last edited:{self.last_edited}, Published:{self.is_published},"


class Student(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    matricnumber = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    program = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"Name: {self.firstname} {self.lastname}, Email: {self.email}, Department: {self.department}, Matric Number: {self.matricnumber}"


