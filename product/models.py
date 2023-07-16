from django.db import models
from category.models import Category
from subcategory.models import SubCategory
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ManyToManyField(SubCategory, blank=False)
    priority = models.IntegerField(default=10)
    active = models.BooleanField(default=True)

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
        return self.name + " - " + str(self.category)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    subImage = models.ImageField(
        upload_to='subImages/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        print("delete")
        # Delete the image from Firebase Storage
        if self.subImage:
            # Get the image path
            image_path = self.subImage.name

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
        return self.product.name + " - " + self.product.category.name


@receiver(pre_delete, sender=Product)
def delete_product_images(sender, instance, **kwargs):
    # Delete associated ProductImage objects
    product_images = ProductImage.objects.filter(product=instance)
    for product_image in product_images:
        product_image.delete()
