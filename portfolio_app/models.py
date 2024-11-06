from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'




