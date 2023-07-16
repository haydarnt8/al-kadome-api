from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100 , blank=False, null=False)
    priority = models.IntegerField(default=10)
    def __str__(self):
        return self.name
    