#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Sets up the product class"

from unitClass import Unit

class Product(Unit):
    '''Represents the product between multiple units'''
    def __init__(self, numList, denomList):
        Unit.__init__(self)
        self.numerator = numList
        self.denominator = denomList


    def count(self):
        '''counts how many units are being simplified'''
        self.unitCount = len(self.numerator) + len(self.denominator)
        return(self.unitCount)

    def cancellable(self):
        '''Find out if the len > 1'''
        if(self.unitCount > 1):
            return True

    def convertNum(self):
        '''Converts all numerators into base units'''
        return(super().baseCheck(self.numerator))

    def convertDenom(self):
        '''Converts all denominators into base units'''
        return(super().baseCheck(self.denominator))

    def simplify(self):
        '''Assume that everything is in base units'''
        pass
