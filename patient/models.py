from django.db import models

# Create your models here.
class Patient(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Name}"