from typing import Union

from fastapi import FastAPI

from app.data import fetch_produts, save_product
from app.models import Product

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Products endpoint


@app.get("/products")
def get_products():
    products = fetch_produts()

    return {"products": products}


@app.post("/products")
def create_product(product: Product):
    save_product(product)
    return {"message": "Product created successfully"}
