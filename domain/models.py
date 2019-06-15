from django.db import models
# from django.conf import settings
#
# # Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Employee(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    email = models.CharField(max_length=256, blank=False, null=False)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
