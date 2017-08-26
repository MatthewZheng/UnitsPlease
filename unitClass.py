#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Sets up the unit class"

class Unit:
    '''This is a class of lists'''
    def __init__(self):
        self.baseUnits = ["m", "kg", "A", "s", "K", "mol", "cd", "rad", "sr"]

    def baseCheck(self, userList):
        '''Converts elements in str list to base units'''
        converted = []
        for i in (userList):
            if(i not in self.baseUnits and len(list(i)) != 1):
                if(len(list(i)) == 1):
                    continue
                orgNameList = list(i)
                #identify prefix removed
                self.idPrefix = orgNameList.pop(0)
                print("The program converted %s to it's base unit --e.g. Gm to m." % self.idPrefix)
                converted.append("".join(orgNameList))
            elif(i in self.baseUnits):
                converted.append(i)
            else:
                print("Your variable %s was not in the commonly used units -- we will assume it is a special unit that is pertinent to your question and add it to the product regardless." % i)
                converted.append(i)
        return(converted)
