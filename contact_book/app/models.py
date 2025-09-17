from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
