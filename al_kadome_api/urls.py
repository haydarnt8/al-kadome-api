"""
URL configuration for al_kadome_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from category.views import categoryController
from product.views import productController
from subcategory.views import subCategoryController
# from product.views import upload_file_to_firebase


api = NinjaAPI()

api.add_router("category/", categoryController)
api.add_router("subcategory/", subCategoryController)
api.add_router("product/", productController)
 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls ),
    # path('upload/', upload_file_to_firebase, name='upload'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)