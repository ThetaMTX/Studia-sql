from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    pesel = models.CharField(max_length=11, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Examination(models.Model):
    patient = models.ForeignKey(Patient, related_name='examinations', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    images = models.ImageField(upload_to='examination_images/', blank=True, null=True)

    def __str__(self):
        return f"Examination on {self.date} for {self.patient.first_name}"
