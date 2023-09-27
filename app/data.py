from app.models import Product

products = [
    Product(
        name="Apple",
        description="An apple a day keeps the doctor away",
        price=0.5,
        tax=0.5,
    ),
    Product(
        name="Pear", description="A pear is a mild, sweet fruit", price=0.5, tax=0.5
    ),
    Product(name="Banana", description="A banana is a tasty fruit", price=0.5, tax=0.5),
    Product(
        name="Kiwi",
        description="A kiwi is a small, fuzzy fruit",
        price=0.5,
        tax=0.5,
    ),
]


def fetch_produts():
    return products


def save_product(product: Product):
    products.append(product)
    return {"message": "Create product"}
