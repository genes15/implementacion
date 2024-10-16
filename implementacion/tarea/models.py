from django.db import models

# Create your models here.

class Task_UNEDepartamento(models.Model):
    name = models.CharField(max_length=60)

class Task_UNEMunicipio(models.Model):
    name = models.CharField(max_length=60)
    Departamento = models.ForeignKey(Task_UNEDepartamento, on_delete=models.CASCADE)

class TypeOrigin(models.Model):
    name = models.CharField(max_length=60)

class Task_Status_Name(models.Model):
    name = models.CharField(max_length=60)
    origin = models.ForeignKey(TypeOrigin, on_delete=models.CASCADE)

class Task_TaskTypeCategory_Name(models.Model):
    name = models.CharField(max_length=60)
    origin = models.ForeignKey(TypeOrigin, on_delete=models.CASCADE)

