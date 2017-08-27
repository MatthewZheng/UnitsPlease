#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Imports all the physics units"

from productClass import Product

#Switchable units
def tryAll(prod):
    #Strip units to base form and assign
    numL = prod.convertNum()
    denomL = prod.convertDenom()

    print("The numerator is", numL, "and the denominator is", denomL)
