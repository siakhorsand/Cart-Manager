#! /usr/bin/env python3

import db
from business import LineItem, Cart

products = db.get_products()
product = products[1]
lineItem = LineItem(product, 2)
cart = Cart()
cart.add_item(lineItem)
print("Product:   ", product.name)
print("Price:     ", product.price)
print("Quantity:  ", lineItem.quantity)
print("Total:     ", cart.get_total())
