from django.contrib import admin
from django import forms
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'subcategory': forms.CheckboxSelectMultiple(),
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    search_fields = ['name', 'description', 'category__name', 'subcategory__name']  # Add search fields
    list_filter = ['subcategory', 'category']  # Add filter by subcategory and category
    form = ProductAdminForm


ProductImageFormSet = forms.inlineformset_factory(
    Product, ProductImage, fields=('subImage',), extra=5
)

admin.site.register(ProductImage)
