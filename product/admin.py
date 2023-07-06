from django.contrib import admin
from .models import Product



admin.site.register(Product)



# from django import forms
# from django.contrib import admin
# from django.utils.html import format_html

# from .models import Product

# class ProductForm(forms.ModelForm):
#     image = forms.ImageField()  # Use ImageField instead of URLField

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Set the image field value to the image URL if an image is uploaded
#         if self.instance.image:
#             self.fields['image'].widget.attrs['value'] = self.instance.image.url

# class ProductAdmin(admin.ModelAdmin):
#     form = ProductForm

#     def save_model(self, request, obj, form, change):
#         # If an image is uploaded, store its URL in the image field
#         if 'image' in form.changed_data and obj.image:
#             obj.image = obj.image.url
#         super().save_model(request, obj, form, change)

#     def image_tag(self, obj):
#         # Display the image in the admin interface
#         return format_html('<img src="{}" width="100" height="100" />', obj.image)

#     image_tag.short_description = 'Image'

#     list_display = ('image_tag',)  # Display the image in the list view

# admin.site.register(Product, ProductAdmin)