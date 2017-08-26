#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Imports all the chemistry units"

from productClass import Product

test = Product(["m", "km", "cm", "K"], ["A", "p", "s"])
print(test.count())
print(test.cancellable())
print(test.convertNum())
print(test.convertDenom())
