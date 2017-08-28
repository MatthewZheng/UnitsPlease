#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Imports all the physics units"

from productClass import Product

#Switchable units
def tryAll(prod):
    #Strip units to base form and assign
    prod.convertNum()
    prod.convertDenom()
    prod.derivedToBase()

    numL = prod.updatedNum
    denomL = prod.updatedDenom

    print("The numerator is", numL, "and the denominator is", denomL)
