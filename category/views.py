from django.shortcuts import render
from ninja import Router
from .models import Category
from subcategory.models import SubCategory
from common.schema import getCategory, getSubCategory
from django.core import serializers
import json

# Create your views here.

categoryController = Router(tags=["Category"])


@categoryController.get("/", response={200: list[getCategory],  404: str})
def get_categories(request):
    try:
        categories = Category.objects.all()
        if not categories:
            return 404, "Category not found"
    except Exception as e:
        return 404, str(e)
    return 200, categories

