
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def categorize(self):
        if self.price >= 50000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.categorize()}")
        print("-" * 35)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully!")

    def display_all(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("\n===== PRODUCT INVENTORY =====")
            for product in self.products:
                product.display()


# Creating Inventory object
inventory = Inventory()

# Creating Product objects
p1 = Product(101, "Laptop", 65000)
p2 = Product(102, "Headphones", 2500)
p3 = Product(103, "Smart TV", 55000)
p4 = Product(104, "Keyboard", 1500)

# Adding products
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)
inventory.add_product(p4)

# Displaying all products
inventory.display_all()