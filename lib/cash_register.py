#!/usr/bin/env python3
class CashRegister:
    def __init__(self):
        self.items = []
        self.total = 0
        self.discount = 0
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.items.append({"title": title, "price": price, "quantity": quantity})
        self.last_transaction = item_cost

    def void_last_transaction(self):
        if self.last_transaction != 0:
            self.total -= self.last_transaction
            self.last_transaction = 0

    def apply_discount(self):
        if self.discount != 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After a {self.discount}% discount, the total comes to ${self.total}."
        else:
            return "There is no discount to apply."


