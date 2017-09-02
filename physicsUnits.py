#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Imports all the physics units"

from productClass import Product

#Switchable units
def tryAll(prod):
    simplifiedN = []
    simplifiedD = []

    #Strip units to base form
    prod.convertUnits()
    prod.derivedToBase()

    #cancel out like units
    prod.cancel()

    #assignment and print values
    numL = prod.updatedNum
    denomL = prod.updatedDenom
    print("OLD: The numerator is", numL, "and the denominator is", denomL)

    if("m" in numL or "m" in denomL):
        #Newtons
        try:
            count = 0
            cont = False
            #determine what units to remove and append simplified to final values
            while(cont == False):
                #modify the external list
                if(all((x in numL for x in ["kg", "m"])) and all(y in denomL for y in ["s", "s"])):
                    simplifiedN.append("N")
                    # count += 1
                    numL.remove("kg")
                    numL.remove("m")
                    denomL.remove("s")
                    denomL.remove("s")

                else:
                    print("okay")
                    cont = True
            # for i in range(count):
            #     numL.remove("kg")
            #     numL.remove("m")
            #     denomL.remove("s")
            #     denomL.remove("s")

            print(numL)
            print(denomL)
            simplifiedN.extend(numL)
            simplifiedD.extend(denomL)

        #values are not present
        except ValueError:
            pass

    print("NEW: The numerator is", simplifiedN, "and the denominator is", simplifiedD)
