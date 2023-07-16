from ninja import Router
from .models import Product, ProductImage
from common.schema import ProductResponse
from django.core.paginator import Paginator
from django.db.models import Q


productController = Router(tags=["Product"])


@productController.get("/", response={200: ProductResponse, 404: str})
def get_product(request, page: int, limit: int, cid: int = None, s_cid: int = None, search: str = None):
    try:
        query = Product.objects.filter(active=True)

        if cid:
            query = query.filter(category__id=cid)
        if s_cid:
            query = query.filter(subcategory__id=s_cid)
        if search:
            query = query.filter(Q(name__icontains=search))

        # Order by priority in ascending order
        query = query.order_by('priority')

        paginator = Paginator(query.only('id', 'name', 'description',
                              'price', 'image', 'category', 'subcategory', 'priority'), limit)
        products = paginator.get_page(page)

        if not products:
            return 404, "Product not found"

        product_list = []

        for product in products:
            images = ProductImage.objects.filter(product=product)
            product_images = []
            for image in images:
                product_images.append({'image': image.image.url})

            product_list.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'image': product.image.url if product.image else None,
                'category': product.category,
                'subcategory': list(product.subcategory.all()),
                'priority': product.priority,
                'images': product_images
            })

    except Exception as e:
        return 404, str(e)

    return 200, {'products': product_list, 'has_next': products.has_next()}
