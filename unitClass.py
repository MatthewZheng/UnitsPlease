#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Sets up the unit class"

class Unit:
    '''This is a class of lists'''
    def __init__(self):
        self.baseUnits = ["m", "kg", "A", "s", "K", "mol", "cd", "L", "C"]

    def baseCheck(self, userList):
        '''Converts elements in str list to base units'''
        converted = []
        for i in (userList):
            #converts non-unary unit to base unit
            if(i not in self.baseUnits and len(list(i)) != 1):
                if(len(list(i)) == 1):
                    continue
                orgNameList = list(i)
                #identify prefix removed
                self.idPrefix = orgNameList.pop(0)
                print("The program removed the prefix %s and converted your unit to it's base unit: %s." % (self.idPrefix, ''.join(orgNameList)))
                converted.append("".join(orgNameList))

            #Appends base unit
            elif(i in self.baseUnits):
                converted.append(i)

            #Exception for special units
            else:
                print("Your variable %s was not in the commonly used units OR it is a derived unit such as N, newtons -- we will add it to the product regardless." % i)
                converted.append(i)
        return(converted)
