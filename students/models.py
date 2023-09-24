from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Consider using a hashed password field instead

    def __str__(self):
        return self.full_name
