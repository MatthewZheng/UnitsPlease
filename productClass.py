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
        self.unitCount = len(self.numerator) + len(self.denominator)


    def count(self, nOrD):
        '''counts how many units are being simplified in either numerator or denominator: n for num, d for denom'''
        if(nOrD.casefold() == "d"):
            return(len(self.denominator))
        elif(nOrD.casefold() == "n"):
            return(len(self.numerator))
        else:
            pass

    def cancellable(self):
        '''Find out if the len > 1'''
        if(self.unitCount > 1):
            return True

    def convertNum(self):
        '''Converts all numerators into base units'''
        self.updatedNum = (super().baseCheck(self.numerator))
        return(self.updatedNum)

    def convertDenom(self):
        '''Converts all denominators into base units'''
        self.updatedDenom = (super().baseCheck(self.denominator))
        return(self.updatedDenom)

    def derivedToBase(self):
        '''This will convert any derived units such as N (newtons), T (teslas), etc to their respective base units. Output: ([num], [denom])'''
        pass
