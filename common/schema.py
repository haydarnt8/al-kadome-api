from ninja import Schema 
from typing import List

class getCategory(Schema):
    id: int
    name: str
    
class getSubCategory(Schema):
    id: int
    name: str
    
class getProduct(Schema):
    id: int
    name: str
    description: str
    price: float
    image: str
    subcategory: List[getSubCategory]
    

class ProductResponse (Schema):
    products: List[getProduct]
    has_next: bool
    





