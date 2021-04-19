from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository


class Shop:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        if product_type == "Drink":
            product = Drink(name)
        elif product_type == "Food":
            product = Food(name)
        self.product_repository.add(product)

    def sell(self, customer_name: str, **shopping_list):
        result = []
        customer = self.customer_repository.find(customer_name)
        if customer == "None":
            new_customer = Customer(customer_name)
            self.customer_repository.add(new_customer)
        for key, value in shopping_list.items():
            product = self.product_repository.find(key)
            if product != "None":
                if product.quantity < value:
                    value = product.quantity
                    self.product_repository.products.remove(product)
                if product in customer.products.keys():
                    customer.products[product] += value
                else:
                    customer.products[product] = value
            result.append(self.product_repository.decrease(product, value))
        return '\n'.join(result)
