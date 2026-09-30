
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def categorize(self):
        if self.price >= 70000:
            return "Premium"
        elif self.price >= 25000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.categorize()}")
        print("-" * 35)


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)
        print("Mobile added successfully!")

    def display_all(self):
        if not self.mobiles:
            print("No mobiles available.")
        else:
            print("\n===== MOBILE STORE =====")
            for mobile in self.mobiles:
                mobile.display()


# Creating Store object
store = Store()

# Creating Mobile objects
m1 = Mobile("Samsung", "Galaxy S25", 79999)
m2 = Mobile("OnePlus", "Nord 5", 29999)
m3 = Mobile("Redmi", "Note 14", 15999)
m4 = Mobile("Apple", "iPhone 16", 69999)

# Adding mobiles
store.add_mobile(m1)
store.add_mobile(m2)
store.add_mobile(m3)
store.add_mobile(m4)

# Displaying all mobiles
store.display_all()