
class Customer:
    def __init__(self, name):
        self.name = name

    def update(self, product, price):
        print(self.name, "received notification:",
              product, "price changed to Rs.", price)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def change_price(self, new_price):
        self.price = new_price
        print("Product price updated!")

        for customer in self.customers:
            customer.update(self.name, self.price)


product = Product("Laptop", 50000)

customer1 = Customer("Maneesha")
customer2 = Customer("Rahul")

product.add_customer(customer1)
product.add_customer(customer2)

product.change_price(45000)
