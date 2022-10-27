from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Student(models.Model):
    STATUS_OF_STUDENT = (
        ('diploma', 'Diploma'),
        ('phd', 'PHD'),
    )
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    age = models.DateTimeField()
    university = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Student')
    status = models.CharField(max_length=30, choices=STATUS_OF_STUDENT, default='diploma')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} From {self.university} University'

    def get_absolute_url(self):
        return reverse("detailsofstudent", kwargs={"pk": self.pk})
    