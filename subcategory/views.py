from django.shortcuts import render
from ninja import Router
from .models import Category, SubCategory
from common.schema import  getSubCategory
from django.core import serializers
import json

subCategoryController = Router(tags=["SubCategory"])

@subCategoryController.get("/", response={200: list[getSubCategory],  404: str})
def get_subcategories(request, cid: int):
    try:
        subcategories = SubCategory.objects.filter(category_id=cid).order_by('priority')
        if not subcategories:
            return 404, "SubCategory not found"
    except Exception as e:
        return 404, str(e)
    return 200, subcategories

