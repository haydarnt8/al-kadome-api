from django.db import models
from category.models import Category

class SubCategory(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    priority = models.IntegerField(default=10)

    def __str__(self):
        return self.name + " - " + self.category.name  + " - " + str(self.id)
