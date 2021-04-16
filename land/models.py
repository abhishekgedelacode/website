from django.db import models

# Create your models here.


class Comments(models.Model):
    email = models.EmailField(max_length=100)
    report = models.TextField()

    def __str__(self):
        return self.email
