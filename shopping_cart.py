#! /usr/bin/env python3

import db
from business import LineItem, Cart


def show_title():
    print("The Shopping Cart Program")
    print()


def show_menu():
    print("COMMAND MENU")
    print("cart - Show the cart")
    print("add - Add an item to the cart ")
    print("del - Delete an item from the cart")
    print("exit - Exit the program")
    print()


def show_products(products):
    print("PRODUCTS")
    header_format = "{:<5s} {:<25s} {:>10s} {:>10s} {:>12s}"
    detail_format = "{:<5d} {:<25s} {:>10.2f} {:>10s} {:>12.2f}"
    print(header_format.format("Item", "Name", "Price",
                               "Discount", "Your Price"))
    for i in range(len(products)):
        product = products[i]
        print(detail_format.format(i + 1, product.name,
                                   product.price, str(product.discount_percent) + "%",
                                   product.get_discount_price()))
        print()


def show_cart(cart):
    if cart.get_item_count() == 0:
        print("There are no items in your cart.\n")
    else:
        header_format = "{:<5s} {:<25s} {:>12s} {:>10s} {:>10s}"
        detail_format = "{:<5d} {:<25s} {:>12.2f} {:>10d} {:10.2f}"
        print(header_format.format("Item", "Name", "Your Price",
                                   "quantity", "Total"))
        i = 0
        for item in cart:
            print(detail_format.format(i + 1, item.product.name,
                                       item.product.get_discount_price(),
                                       item.quantity, item.get_total()))
            i += 1
        print("{:>66.2f}".format(cart.get_total()))
        print()


def add_item(cart, products):
    number = int(input("Input number: "))
    quantity = int(input("Quantity: "))
    if number < 1 or number > len(products):
        print("No product has that number.\n")
    else:
        product = products[number - 1]
        item = LineItem(product, quantity)
        cart.add_item(item)
        print("Item" + str(cart.get_item_count()) + " was added.\n")


def remove_item(cart):
    number = int(input("Input number: "))
    if number < 1 or number > cart.get_item_count():
        print("The cart does not contain an item" + "with that item number\n")
    else:
        cart.remove_item(number - 1)
        print("Item " + str(number) + " was removed from cart.\n")


def main():
    show_title()
    show_menu()

    products = db.get_products()
    show_products(products)

    cart = Cart()
    while True:
        command = input("Command: ")
        if command == "cart":
            show_cart(cart)
        elif command == "add":
            add_item(cart, products)
        elif command == "del":
            remove_item(cart)
        elif command == "exit":
            print("CYA")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
