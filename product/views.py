from django.shortcuts import render
from ninja import Router
from .models import Product
from common.schema import ProductResponse, getProduct
import json
from django.core import serializers
# import paginater
from django.core.paginator import Paginator
from django.db.models import Q


productController = Router(tags=["Product"])


@productController.get("/", response={200: ProductResponse,  404: str})
def get_product(request, page: int, limit: int, cid: int = None, s_cid: int = None, search: str = None):
    try:
        query = Product.objects.all()

        if cid:
            query = query.filter(category__id=cid)
        if s_cid:
            query = query.filter(subcategory__id=s_cid)
        if search:
            query = query.filter(Q(name__icontains=search))

        paginator = Paginator(query.only('id', 'name', 'price'), limit)
        products = paginator.get_page(page)

        if not products:
            return 404, "Product not found"
    except Exception as e:
        return 404, str(e)

    return 200, { 'products': list(products.object_list), 'has_next': products.has_next()}




# from django.http import HttpResponse
# from firebase_admin import storage

# def upload_file_to_firebase(request):
#     # Assuming you have a file stored locally that you want to upload
#     file_path = 'D:test.txt'
#     destination_path = 'files/file.txt'  # Destination path in Firebase Storage

#     # Upload the file to Firebase Storage
#     bucket = storage.bucket()
#     blob = bucket.blob(destination_path)
#     blob.upload_from_filename(file_path)

#     return HttpResponse('File uploaded to Firebase Storage!')

