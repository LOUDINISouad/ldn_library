from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=1000, default="")
 

    def __str__(self):
        return self.title
