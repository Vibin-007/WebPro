from django.db import models


class Todo(models.Model):
   content = models.TextField()

class EventRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    event_name = models.CharField(max_length=100)
    event_category = models.CharField(max_length=100)
    event_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.event_name}"


class Student(models.Model):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
