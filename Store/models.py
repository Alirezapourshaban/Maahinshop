from __future__ import unicode_literals
from django.db import models

# Create your models here.
class HeaderTitle(models.Model):
    title = models.CharField('title', max_length=70)


class Product(models.Model):
        title=models.CharField(max_length=150)
        slug=models.SlugField()
        body=models.TextField()
        date=models.DateTimeField(auto_now_add=True)
        category=models.CharField(max_length=100)
        features=models.TextField()
        specification=models.TextField()
        discription=models.TextField()
        def __str__(self):
          return self.title