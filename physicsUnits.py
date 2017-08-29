#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Imports all the physics units"

from productClass import Product

#Switchable units
def tryAll(prod):
    #Strip units to base form
    prod.convertUnits()
    prod.derivedToBase()

    #cancel out like units
    prod.cancel()

    #assignment ad print values
    numL = prod.updatedNum
    denomL = prod.updatedDenom
    print("The numerator is", numL, "and the denominator is", denomL)
