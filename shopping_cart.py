
from ensurepip import version


class ShoppingCart:

    def __init__(self):
        self.cart = []

    def number_of_products(self):
        total_number_of_products = len(self.cart)
        return total_number_of_products

    def add_items_to_cart(self, product):
        self.cart.append(product)

    def remove_all_from_cart(self):
        del self.cart