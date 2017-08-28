#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Sets up the unit class"

class Unit:
    '''This is a class of lists'''
    def __init__(self):
        self.baseUnits = ["m", "kg", "A", "s", "K", "mol", "cd", "sr", "rad"]
        self.derivedUnits = ["Hz", "N", "Pa", "J", "W", "C", "V", "F", "ohm", "S", "Wb", "T", "H", "°C", "lm", "lx", "Bq", "Gy", "Sv", "kat"]

    def baseCheck(self, userList):
        '''Converts elements in str list to base units'''
        converted = []

        for i in (userList):
            isSquared = False
            unitPreIndex = ""

            #checks if it has a carat in the expression
            for ind, j in enumerate(list(i)):
                if j == "^":
                    isSquared = True
                    unitPreIndex = ''.join(list(i)[:ind])
                    # print("is squared lol")
                    break

            #converts non-unary unit to base unit and checks for squared variables
            while(i not in (self.baseUnits and self.derivedUnits) and len(list(i)) != 1 and unitPreIndex not in (self.baseUnits and self.derivedUnits) and len(unitPreIndex) != 1):
                orgNameList = list(i)
                #identify prefix removed
                self.idPrefix = orgNameList.pop(0)
                i = ''.join(orgNameList)
                print("The program removed the prefix %s and converted your unit to it's base unit: %s." % (self.idPrefix, i))
                #checks if it is a special unit
                if(i not in (self.baseUnits and self.derivedUnits)):
                    #append in case for special units
                    break
                else:
                    #append in case for base unit
                    break

            #Appends base unit
            if(i in (self.baseUnits and self.derivedUnits) and isSquared == False):
                converted.append(i)

            elif(isSquared == True):
                toAppend = []
                numReps = []

                #run once to get number of times the unit is squared
                for index, val in enumerate(list(i)):
                    if val == "^":
                        numStart = index+1
                        numReps.append(''.join(list(i)[numStart:]))
                        toAppend.append(''.join(list(i)[:index]))
                        break

                #convert numReps into an int
                intReps = int(''.join(numReps))

                #append number of units specified by the carat
                for l in range (intReps):
                    if(''.join(toAppend) not in (self.baseUnits and self.derivedUnits)):
                        print("Your variable %s was not in the commonly used units OR it is a derived unit such as N, newtons -- we will add it to the product regardless." % ''.join(toAppend))
                    converted.append(''.join(toAppend))


            #Exception for special units
            else:
                print("Your variable %s was not in the commonly used units OR it is a derived unit such as N, newtons -- we will add it to the product regardless." % i)
                converted.append(i)

        return(converted)
