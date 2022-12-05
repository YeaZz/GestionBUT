from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Establishment(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Department(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, default=None, blank=False, null=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name;

class UsefulLink(models.Model):
    name=models.CharField(max_length=30)
    file_path=models.CharField(max_length=50)
    link=models.CharField(max_length=70)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name;

class BUT(models.Model):
    type=models.CharField(max_length=50)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.type

class Course(models.Model):
    BUT = models.ManyToManyField(BUT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UE(models.Model):
    number=models.IntegerField(default=None, blank=False, null=True)
    description=models.CharField(max_length=500, default="")

    def __str__(self):
        return "UE" + str(self.number) + " - " + self.description

class Resource(models.Model):
    name=models.CharField(max_length=50)
    ue=models.ManyToManyField(UE)

    def __str__(self):
        return self.name;

class Semester(models.Model):
    number=models.IntegerField(default=None, blank=False, null=True)
    ue=models.ManyToManyField(UE)

    def __str__(self):
        return "S" + str(self.number)

class Year(models.Model):
    name=models.CharField(max_length=70)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, blank=True, null=True)
    first_semester=models.ForeignKey(Semester, related_name="first_semester", on_delete=models.CASCADE, default=None, blank=False, null=True)
    second_semester=models.ForeignKey(Semester, related_name="second_semester", on_delete=models.CASCADE, default=None, blank=False, null=True)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name=models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)
    year=models.ForeignKey(Year, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    group=models.ManyToManyField(Group)

    def __str__(self):
        return self.id.username
        
class Professor(models.Model):
    id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=False)
    resource=models.ManyToManyField(Resource)

    def __str__(self):
        return self.id.username

class Competence(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    ue=models.ForeignKey(UE, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name;
