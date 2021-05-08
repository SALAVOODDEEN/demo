"""
models required for the hospital project
"""
from django.db import models

# Create your models here.


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    status = models.BooleanField(default=True, null=True)
    description = models.CharField(max_length=50)
    department_created_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.department_name


class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    phone_no = models.IntegerField(null=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



"""
book appointment for patients takes the data from the UI
"""
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True, null=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.appointment_id


