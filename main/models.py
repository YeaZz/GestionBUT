from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name;

class Establishment(models.Model):
    name = models.CharField(max_length=80)
    departments = models.ManyToManyField(Department, blank=False, related_name="establishments")

    def __str__(self):
        return self.name

class UsefulLink(models.Model):
    name = models.CharField(max_length=30)
    file_path = models.CharField(max_length=50)
    link = models.CharField(max_length=70)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name;

class BUT(models.Model):
    type = models.CharField(max_length=50)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.type

class Course(models.Model):
    BUTs = models.ManyToManyField(BUT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UE(models.Model):
    number = models.IntegerField(default=None, blank=False, null=True)
    description = models.CharField(max_length=500, default="")

    def __str__(self):
        return "UE" + str(self.number) + " - " + self.description

class Resource(models.Model):
    name = models.CharField(max_length=50)
    ues = models.ManyToManyField(UE)

    def __str__(self):
        return self.name

class Semester(models.Model):
    number = models.IntegerField(default=None, blank=False, null=True)
    ues = models.ManyToManyField(UE)

    def __str__(self):
        return "S" + str(self.number)

class Year(models.Model):
    name = models.CharField(max_length=70)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, blank=True, null=True)
    first_semester = models.ForeignKey(Semester, related_name="first_semester", on_delete=models.CASCADE, default=None, blank=False, null=True)
    second_semester = models.ForeignKey(Semester, related_name="second_semester", on_delete=models.CASCADE, default=None, blank=False, null=True)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.id.username

class Professor(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    establishments = models.ManyToManyField(Establishment, blank=False)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.id.username

class Administrator(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    establishments = models.ManyToManyField(Establishment, blank=False)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.id.username

class Competence(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name;

import math

class Evaluation(models.Model):
    name = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, default=None, blank=False, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=None, blank=False, null=True)
    ue = models.ManyToManyField(UE, blank=False)

    def __str__(self):
        return self.name;
    
    def calcAverage(self):
        grades = Grade.objects.all().filter(evaluation=self.id)
        if grades.count() <= 0:
            return None
        sum = 0
        for grade in grades.all():
            sum += grade.note
        return sum / grades.count()
    
    def calcMax(self):
        grades = Grade.objects.all().filter(evaluation=self.id)
        if grades.count() <= 0:
            return None
        max = -math.inf
        for grade in grades.all():
            if max > grade.note:
                max = grade.note
        return max

    def calcMinus(self):
        grades = Grade.objects.all().filter(evaluation=self.id)
        if grades.count() <= 0:
            return None
        min = math.inf
        for grade in grades.all():
            if min > grade.note:
                min = grade.note
        return min

class Grade(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, default=None, blank=False, null=True)
    note = models.FloatField(default=0.0, blank=False, null=False)
    coef = models.FloatField(default=1.0, blank=True, null=False)

    def calcNote(self):
        return self.note * self.coef;

def loadInformatique():
    department = Department(name="Informatique")
    department.save()

    establishment = Establishment(name="IUT Claude Bernard Lyon 1 - Bourg en bresse")
    establishment.save()
    establishment.departments.add(department)

    ue1_1 = UE(number=1, description="Développer des applications informatiques simples")
    ue1_1.save()
    ue1_2 = UE(number=1, description="Partir des exigences et aller jusqu'à une application complète")
    ue1_2.save()
    ue1_3 = UE(number=1, description="Adapter des applications sur un ensemble de supports (embarqué, web, mobile, IoT…)")
    ue1_3.save()

    ue2_1 = UE(number=2, description="Appréhender et construire des algorithmes")
    ue2_1.save()
    ue2_2 = UE(number=2, description="Sélectionner les algorithmes adéquats pour répondre à un problème donné")
    ue2_2.save()
    ue2_3 = UE(number=2, description="Analyser et optimiser des applications")
    ue2_3.save()

    ue3_1 = UE(number=3, description="Installer et configurer un poste de travail")
    ue3_1.save()
    ue3_2 = UE(number=3, description="Déployer des services dans une architecture réseau")
    ue3_2.save()
    ue3_3 = UE(number=3, description="Faire évoluer et maintenir un système informatique communicant en conditions opérationnelles")
    ue3_3.save()

    ue4_1 = UE(number=4, description="Concevoir et mettre en place une base de données à partir d'un cahier des charges client")
    ue4_1.save()
    ue4_2 = UE(number=4, description="Optimiser une base de données, interagir avec une application et mettre en œuvre la sécurité")
    ue4_2.save()
    ue4_3 = UE(number=4, description="Administrer une base de données, concevoir et réaliser des systèmes d'informations décisionnels")
    ue4_3.save()

    ue5_1 = UE(number=5, description="Identifier les besoins métiers des clients et des utilisateurs")
    ue5_1.save()
    ue5_2 = UE(number=5, description="Appliquer une démarche de suivi de projet en fonction des besoins métiers des clients et des utilisateurs")
    ue5_2.save()
    ue5_3 = UE(number=5, description="Participer à la conception et à la mise en oeuvre d'un projet système d'information")
    ue5_3.save()
    
    ue6_1 = UE(number=6, description="Identifier ses aptitudes pour travailler dans une équipe")
    ue6_1.save()
    ue6_2 = UE(number=6, description="Situer son rôle et ses missions au sein d'une équipe informatique")
    ue6_2.save()
    ue6_3 = UE(number=6, description="Manager une équipe informatique")
    ue6_3.save()

    semester1 = Semester(number=1)
    semester1.save()
    semester1.ues.add(ue1_1, ue2_1, ue3_1, ue4_1, ue5_1, ue6_1)
    semester2 = Semester(number=2)
    semester2.save()
    semester2.ues.add(ue1_1, ue2_1, ue3_1, ue4_1, ue5_1, ue6_1)

    semester3 = Semester(number=3)
    semester3.save()
    semester3.ues.add(ue1_2, ue2_2, ue3_2, ue4_2, ue5_2, ue6_2)
    semester4 = Semester(number=4)
    semester4.save()
    semester4.ues.add(ue1_2, ue2_2, ue3_2, ue4_2, ue5_2, ue6_2)

    semester5 = Semester(number=5)
    semester5.save()
    semester5.ues.add(ue1_3, ue2_3, ue3_3, ue4_3, ue5_3, ue6_3)
    semester6 = Semester(number=6)
    semester6.save()
    semester6.ues.add(ue1_3, ue2_3, ue3_3, ue4_3, ue5_3, ue6_3)

    year1 = Year(name="Première année", first_semester=semester1, second_semester=semester2)
    year1.save()
    year2 = Year(name="Première année", first_semester=semester3, second_semester=semester4)
    year2.save()
    year3 = Year(name="Première année", first_semester=semester5, second_semester=semester6)
    year3.save()

    groupS1 = Group(name="S1", department=department, parent=None, year=year1)
    groupS1.save()
    groupS1G1 = Group(name="S1G1", department=department, parent=groupS1, year=year1)
    groupS1G1.save()
    groupS1G1_1 = Group(name="S1G1.1", department=department, parent=groupS1, year=year1)
    groupS1G1_1.save()

    noa = Student(id=User.objects.all().filter(username="noa_cavalcante").first())
    noa.save()
    noa.groups.add(groupS1, groupS1G1, groupS1G1_1)

    lilian = Student(id=User.objects.all().filter(username="lilian_ouraha").first())
    lilian.save()
    lilian.groups.add(groupS1, groupS1G1, groupS1G1_1)

    corto = Student(id=User.objects.all().filter(username="corto_bouviolle").first())
    corto.save()
    corto.groups.add(groupS1, groupS1G1, groupS1G1_1)

    peytavie = Professor(id=User.objects.all().filter(username="adrien_peytavie").first())
    peytavie.save()
    peytavie.establishments.add(establishment)

def empty():
    Professor.objects.all().delete()
    Student.objects.all().delete()
    Group.objects.all().delete()
    Year.objects.all().delete()
    Semester.objects.all().delete()
    UE.objects.all().delete()
    Department.objects.all().delete()
    Establishment.objects.all().delete()