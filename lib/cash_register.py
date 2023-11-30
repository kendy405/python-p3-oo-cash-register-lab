#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prices = []

  def add_item(self, title, price, quantity=1):
    for i in range(quantity):
      self.items.append(title)
    self.prices.append(price*quantity)
    self.total += price*quantity

  def apply_discount(self):
    if(self.discount > 0):
      self.total -= self.total*self.discount/100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.prices[len(self.prices)-1]
    self.items.pop()
