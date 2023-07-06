from django.db import models
from category.models import Category

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.category.name  + " - " + str(self.id)
