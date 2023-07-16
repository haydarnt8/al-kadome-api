from ninja import Schema
from typing import List, Optional


class getCategory(Schema):
    id: int
    name: str


class getSubCategory(Schema):
    id: int
    name: str


class getProductImage(Schema):
    image: str


class getProduct(Schema):
    id: int
    name: str
    description: str
    price: float
    image: Optional[str]
    category: getCategory
    subcategory: List[getSubCategory]
    priority: int
    images: List[getProductImage]


class ProductResponse (Schema):
    products: List[getProduct]
    has_next: bool
