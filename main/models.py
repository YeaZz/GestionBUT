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
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.type

class Course(models.Model):
    BUTs = models.ManyToManyField(BUT)
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
    ues=models.ManyToManyField(UE)

    def __str__(self):
        return self.name;

class Semester(models.Model):
    number=models.IntegerField(default=None, blank=False, null=True)
    ues=models.ManyToManyField(UE)

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
    groups=models.ManyToManyField(Group)

    def __str__(self):
        return self.id.username
        
class Professor(models.Model):
    id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
<<<<<<< HEAD
    department=models.ManyToManyField(Department)
    resource=models.ManyToManyField(Resource ,blank=True)
=======
    departments=models.ManyToManyField(Department, blank=False)
    resources=models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.id.username

class Administrator(models.Model):
    id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    departments=models.ManyToManyField(Department, blank=False)
    resources=models.ManyToManyField(Resource, blank=True)
>>>>>>> cf257c996ac6271d829708a7d9ac7cb76bb62d75

    def __str__(self):
        return self.id.username

class Competence(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    ue=models.ForeignKey(UE, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name;
