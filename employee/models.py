from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Enter full name")
    email = models.EmailField(help_text="Enter email address")
    phone = models.CharField(max_length=15, help_text="Enter contact number")
    position = models.CharField(max_length=100, help_text="Enter job title")

    class Meta:
        ordering = ['name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.name} - {self.position}"
