from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    sub = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
