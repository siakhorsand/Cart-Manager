#! /usr/bin/env python3

class Product:
    def __init__(self, name="", price=0.0, discount_percent=0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def get_discount_amount(self):
        discount_amount = self.price * self.discount_percent / 100
        return round(discount_amount, 2)

    def get_discount_price(self):
        discount_price = self.price - self.get_discount_amount()
        return round(discount_price, 2)


class LineItem:
    def __init__(self, product=None, quantity=1):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        total = self.product.get_discount_price() * self.quantity
        return total


class Cart:
    def __init__(self):
        self.__lineItems = []

    def add_item(self, item):
        self.__lineItems.append(item)

    def remove_item(self, index):
        self.__lineItems.pop(index)

    def get_total(self):
        total = 0.0
        for item in self.__lineItems:
            total += item.get_total()
        return total

    def get_item_count(self):
        return len(self.__lineItems)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineItems) - 1:
            raise StopIteration
        self.__index += 1
        line_item = self.__lineItems[self.__index]
        return line_item
