from functions.Product import Product
import json

class ProductRepository:
    def __init__(self):
        self.dataFile = "products.json"
        self.products = {}

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added.")
        self.products[product.id] = product

    def get_product(self, product_id):
        return self.products.get(product_id)

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def update_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be updated.")
        if product.id in self.products:
            self.products[product.id] = product

    def list_products(self):
        return list(self.products.values())

    def __loadFromJson__(self, json_data):
        data = json.loads(json_data)
        for item in data:
            product = Product(**item)
            self.add_product(product)
    
    def __saveToJson__(self):
        return json.dumps([product.to_dict() for product in self.products.values()])
    
    def load(self):
        try:
            with open(self.dataFile, 'r') as file:
                json_data = file.read()
                self.__loadFromJson__(json_data)
        except FileNotFoundError:
            print(f"File {self.dataFile} not found. Starting with an empty repository.")
    
    def save(self):
        with open(self.dataFile, 'w') as file:
            json_data = self.__saveToJson__()
            file.write(json_data)