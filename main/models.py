import math
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Establishment(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def getDepartments(self):
        return Department.objects.filter(establishment=self)

class Department(models.Model):
    name = models.CharField(max_length=80)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name

    def getSemesters(self):
        return Semester.objects.filter(department=self).order_by("number")

    def getGroups(self):
        return Group.objects.filter(department=self).order_by("name")

    def getStudents(self):
        return Student.objects.filter(department=self)

    def getUsefulLinks(self):
        return UsefulLink.objects.filter(department=self).order_by("name")

class UsefulLink(models.Model):
    name = models.CharField(max_length=30)
    file_path = models.CharField(max_length=50)
    link = models.CharField(max_length=70)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name

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

    def getName(self, semester):
        return "UE" + str(semester.number) + "." + str(self.number)

    def getResources(self):
        return Resource.objects.filter(ues=self).order_by("number")

    def getNote(self, student):
        nb, sum = 0, 0
        resources = Resource.objects.filter(ues=self)
        for resource in resources:
            for evaluation in resource.getEvaluations():
                note = evaluation.getNote(student)
                if note != None:
                    sum += note
                    nb += 1
        return round(sum / nb, 2) if nb > 0 else None

    def getRanking(self, student):
        notes = {}
        students = student.department.getStudents()
        for s in students:
            note = self.getNote(s)
            if note != None:
                notes[s] = note
        if len(notes) > 0:
            notes = dict(sorted(notes.items(), key=lambda notes:notes[1], reverse=True))
            index = list(notes.keys()).index(student)
            return str(index + 1) + "/" + str(len(notes))
        return None

class Semester(models.Model):
    number = models.IntegerField(default=None, blank=False, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return "S" + str(self.number)

    def getResources(self):
        return Resource.objects.filter(semester=self).order_by("number")

    def getUEs(self):
        ues = []
        for resource in self.getResources():
            for ue in resource.ues.all():
                if ue not in ues:
                    ues.append(ue)
        return ues

class Resource(models.Model):
    number = models.IntegerField(default=None, blank=False, null=True)
    name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=None, blank=False, null=True)
    ues = models.ManyToManyField(UE, related_name="resources")

    def __str__(self):
        return f"R{self.semester.number}.{self.number} {self.name}"

    def getEvaluations(self):
        return Evaluation.objects.filter(resource=self)

    def getNote(self, student):
        nb, sum = 0, 0
        for evaluation in self.getEvaluations():
            note = evaluation.getNote(student)
            if note != None:
                sum += note
                nb += 1
        return sum / nb if nb > 0 else None

    def getRanking(self, student):
        notes = {}
        for s in student.department.getStudents():
            note = self.getNote(s)
            if note != None:
                notes[s] = note
        if len(notes) > 0:
            notes = dict(sorted(notes.items(), key=lambda notes:notes[1], reverse=True))
            index = list(notes.keys()).index(student)
            return str(index + 1) + "/" + str(len(notes))
        return None

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
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="children")
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name

    def getDepartmentTree(department):
        tree = {}
        for child in Group.objects.filter(parent=None, department=department):
            tree[child] = child.getTree()
        return tree

    def getTree(self):
        if len(self.children.all()) == 0:
            return {}
        group = {self: {}}
        for child in self.children.order_by("name"):
            group[self].update(child.getTree())
        return group

class Student(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=False, null=True)
    groups = models.ManyToManyField(Group, blank=False, related_name="students")

    def __str__(self):
        return self.id.username

    def getGrades(self):
        return Grade.objects.filter(student=self)

    def getLastGrades(self, amount):
        return self.getGrades()[:amount]

class Professor(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return f"{self.id.first_name} {self.id.last_name}"

    def getResources(self, department):
        resources = []
        for resource in self.resources.all():
            if resource.semester.department == department:
                resources.append(resource)
        return resources

    def getDepartments(self):
        departments = []
        for resource in self.resources.all():
            if resource.semester.department not in departments:
                departments.append(resource.semester.department)
        return departments

    def getEtablishments(self):
        establishments = []
        for department in self.getDepartments():
            if department.establishment not in establishments:
                establishments.append(department.establishment)
        return establishments

class Administrator(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.id.username

class Competence(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    name = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, default=None, blank=False, null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def __str__(self):
        return self.name

    def getGrades(self):
        return Grade.objects.filter(evaluation=self)

    def getGrade(self, student):
        return Grade.objects.filter(evaluation=self, student=student)

    def getNote(self, student):
        grades = self.getGrade(student)
        return grades.first().note if len(grades) == 1 else None

    def getAverage(self):
        grades = self.getGrades()
        if len(grades) <= 0:
            return None
        sum = 0
        for grade in grades:
            sum += grade.note
        return round(sum / len(grades), 2)

    def getMax(self):
        grades = self.getGrades()
        if len(grades) <= 0:
            return None
        max = -math.inf
        for grade in grades:
            if max < grade.note:
                max = grade.note
        return max

    def getMin(self):
        grades = self.getGrades()
        if len(grades) <= 0:
            return None
        min = math.inf
        for grade in grades:
            if min > grade.note:
                min = grade.note
        return min

    def getRanking(self, student):
        notes = {}
        for s in student.department.getStudents():
            note = self.getNote(s)
            if note != None:
                notes[s] = note
        if len(notes) > 0:
            notes = dict(sorted(notes.items(), key=lambda notes:notes[1], reverse=True))
            index = list(notes.keys()).index(student)
            return str(index + 1) + "/" + str(len(notes))
        return None

class Grade(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, default=None, blank=False, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None, blank=False, null=True)
    note = models.FloatField(default=0.0, blank=False, null=False)
    coef = models.FloatField(default=1.0, blank=True, null=False)

    def __str__(self):
        return self.evaluation.name

    def calcNote(self):
        return self.note * self.coef

def load():
    empty()

    establishment = Establishment(name="IUT Claude Bernard Lyon 1 - Bourg en bresse")
    establishment.save()

    department = Department(name="Informatique", establishment=establishment)
    department.save()

    moodle = UsefulLink(name="Moodle", file_path="img/moodle.png", link="https://moodle.univ-lyon1.fr/", department=department)
    moodle.save()
    mail = UsefulLink(name="Mail", file_path="img/mail.png", link="https://mail.univ-lyon1.fr/", department=department)
    mail.save()

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

    semester1 = Semester(number=1, department=department)
    semester1.save()
    semester2 = Semester(number=2, department=department)
    semester2.save()

    semester3 = Semester(number=3, department=department)
    semester3.save()
    semester4 = Semester(number=4, department=department)
    semester4.save()

    semester5 = Semester(number=5, department=department)
    semester5.save()
    semester6 = Semester(number=6, department=department)
    semester6.save()

    resource1 = Resource(number="1", name="Initiation au dev.", semester=semester1)
    resource1.save()
    resource1.ues.add(ue1_1, ue3_1)

    resource2 = Resource(number="2", name="Développement d'interfaces web", semester=semester1)
    resource2.save()
    resource2.ues.add(ue1_1, ue5_1, ue6_1)

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
    groupS1G1_1 = Group(name="S1G1.1", department=department, parent=groupS1G1, year=year1)
    groupS1G1_1.save()
    groupS1G1_2 = Group(name="S1G1.2", department=department, parent=groupS1G1, year=year1)
    groupS1G1_2.save()

    groupS2 = Group(name="S2", department=department, parent=None, year=year1)
    groupS2.save()
    groupS2G1 = Group(name="S2G1", department=department, parent=groupS2, year=year1)
    groupS2G1.save()
    groupS2G1_1 = Group(name="S2G1.1", department=department, parent=groupS2G1, year=year1)
    groupS2G1_1.save()
    groupS2G1_2 = Group(name="S2G1.2", department=department, parent=groupS2G1, year=year1)
    groupS2G1_2.save()

    noa = Student(id=User.objects.all().filter(username="noa_cavalcante").first(), department=department)
    noa.save()
    noa.groups.add(groupS1, groupS1G1, groupS1G1_1)

    lilian = Student(id=User.objects.all().filter(username="lilian_ouraha").first(), department=department)
    lilian.save()
    lilian.groups.add(groupS1, groupS1G1, groupS1G1_1)

    corto = Student(id=User.objects.all().filter(username="corto_bouviolle").first(), department=department)
    corto.save()
    corto.groups.add(groupS1, groupS1G1, groupS1G1_2)

    peytavie = Professor(id=User.objects.all().filter(username="adrien_peytavie").first())
    peytavie.save()
    peytavie.resources.add(resource1, resource2)

    administrator = Administrator(id=User.objects.all().filter(username="administrateur").first())
    administrator.save()

    evaluation = Evaluation(name="TP 1", professor=peytavie, resource=resource1)
    evaluation.save()

    grade = Grade(evaluation=evaluation, student=noa, note=20.0)
    grade.save()
    grade = Grade(evaluation=evaluation, student=corto, note=4.0)
    grade.save()
    grade = Grade(evaluation=evaluation, student=lilian, note=1.5)
    grade.save()

    evaluation = Evaluation(name="TP 2", professor=peytavie, resource=resource1)
    evaluation.save()

    grade = Grade(evaluation=evaluation, student=noa, note=16.0)
    grade.save()
    grade = Grade(evaluation=evaluation, student=corto, note=10.0)
    grade.save()
    grade = Grade(evaluation=evaluation, student=lilian, note=11.5)
    grade.save()

def empty():
    Professor.objects.all().delete()
    Student.objects.all().delete()
    Group.objects.all().delete()
    Year.objects.all().delete()
    Semester.objects.all().delete()
    UE.objects.all().delete()
    Department.objects.all().delete()
    Establishment.objects.all().delete()