from django.db import models
from category.models import Category
from subcategory.models import SubCategory


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ManyToManyField(SubCategory)

    def delete(self, *args, **kwargs):
        # Delete the image from Firebase Storage
        if self.image:
            # Get the image path
            image_path = self.image.name

            from firebase_admin import storage
            from django.core.files.storage import default_storage

            # Get the default Firebase storage bucket
            bucket = storage.bucket()

            # Delete the image blob from Firebase Storage
            blob = bucket.blob(image_path)
            blob.delete()

            # Delete the image file from local storage
            default_storage.delete(image_path)

            # Delete the database record
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.name + " - " + self.category.name
