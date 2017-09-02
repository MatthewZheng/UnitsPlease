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


    #############Begin unit conversion cases####################################
    if("m" in numL or "m" in denomL):

        # #Watts
        # try:
        #     count = 0
        #     cont = False
        #     #determine what units to remove and append simplified to final values
        #     while(cont == False):
        #         #modify the external list
        #         if(all((x in numL for x in ["kg", "m", "m"])) and all(y in denomL for y in ["s", "s", "s"])):
        #             simplifiedN.append("W")
        #             count += 1
        #             numL.remove("kg")
        #             numL.remove("m")
        #             numL.remove("m")
        #             denomL.remove("s")
        #             denomL.remove("s")
        #             denomL.remove("s")
        #         else:
        #             cont = True
        #     #assignment only occurs when the conditional for the base units are met
        #     if count > 0:
        #         print(numL)
        #         print(denomL)
        #         simplifiedN.extend(numL)
        #         simplifiedD.extend(denomL)
        # #values are not present
        # except ValueError:
        #     pass
        #
        # #Check for inverted unit
        # try:
        #     count = 0
        #     cont = False
        #     while(cont == False):
        #         #modify the external list
        #         if(all((j in denomL for j in ["kg", "m", "m"])) and all(k in numL for k in ["s", "s", "s"])):
        #             simplifiedD.append("W")
        #             count += 1
        #             denomL.remove("kg")
        #             denomL.remove("m")
        #             denomL.remove("m")
        #             numL.remove("s")
        #             numL.remove("s")
        #             numL.remove("s")
        #         else:
        #             cont = True
        #     if count > 0:
        #         print(numL)
        #         print(denomL)
        #         simplifiedN.extend(numL)
        #         simplifiedD.extend(denomL)
        # #values are not present
        # except ValueError:
        #     pass
        #
        # #Joules
        # try:
        #     count = 0
        #     cont = False
        #     #determine what units to remove and append simplified to final values
        #     while(cont == False):
        #         #modify the external list
        #         if(all((x in numL for x in ["kg", "m", "m"])) and all(y in denomL for y in ["s", "s"])):
        #             simplifiedN.append("J")
        #             count += 1
        #             numL.remove("kg")
        #             numL.remove("m")
        #             numL.remove("m")
        #             denomL.remove("s")
        #             denomL.remove("s")
        #         else:
        #             cont = True
        #     #assignment only occurs when the conditional for the base units are met
        #     if count > 0:
        #         print(numL)
        #         print(denomL)
        #         simplifiedN.extend(numL)
        #         simplifiedD.extend(denomL)
        # except ValueError:
        #     pass
        #
        # try:
        #     count = 0
        #     cont = False
        #     while(cont == False):
        #         #modify the external list
        #         if(all((j in denomL for j in ["kg", "m", "m"])) and all(k in numL for k in ["s", "s"])):
        #             simplifiedD.append("J")
        #             count += 1
        #             denomL.remove("kg")
        #             denomL.remove("m")
        #             denomL.remove("m")
        #             numL.remove("s")
        #             numL.remove("s")
        #         else:
        #             cont = True
        #     if count > 0:
        #         print(numL)
        #         print(denomL)
        #         simplifiedN.extend(numL)
        #         simplifiedD.extend(denomL)
        # except ValueError:
        #     pass
        #
        #
        # #Pascals
        # try:
        #     count = 0
        #     cont = False
        #     while(cont == False):
        #         if(all((x in numL for x in ["kg"])) and all(y in denomL for y in ["m", "s", "s"])):
        #             simplifiedN.append("Pa")
        #             count += 1
        #             numL.remove("kg")
        #             denomL.remove("m")
        #             denomL.remove("s")
        #             denomL.remove("s")
        #         else:
        #             cont = True
        #     if count > 0:
        #         print(numL)
        #         print(denomL)
        #         simplifiedN.extend(numL)
        #         simplifiedD.extend(denomL)
        # except ValueError:
        #     pass
        #
        # try:
        #     count = 0
        #     cont = False
        #     while(cont == False):
        #         if(all((j in denomL for j in ["kg"])) and all(k in numL for k in ["m", "s", "s"])):
        #             simplifiedD.append("Pa")
        #             count += 1
        #             denomL.remove("kg")
        #             numL.remove("m")
        #             numL.remove("s")
        #             numL.remove("s")
        #         else:
        #             cont = True
        #     if count > 0:
        #         print(numL)
        #         print(denomL)
        #         simplifiedN.extend(numL)
        #         simplifiedD.extend(denomL)
        # except ValueError:
        #     pass

        #Newtons
        try:
            count = 0
            cont = False
            while(cont == False):
                if(all((x in numL for x in ["kg", "m"])) and all(y in denomL for y in ["s", "s"])):
                    simplifiedN.append("N")
                    count += 1
                    numL.remove("kg")
                    numL.remove("m")
                    denomL.remove("s")
                    denomL.remove("s")
                else:
                    cont = True
            if count > 0:
                print(numL)
                print(denomL)
                simplifiedN.extend(numL)
                simplifiedD.extend(denomL)
        except ValueError:
            pass

        try:
            count = 0
            cont = False
            while(cont == False):
                if(all((j in denomL for j in ["kg", "m"])) and all(k in numL for k in ["s", "s"])):
                    simplifiedD.append("N")
                    count += 1
                    denomL.remove("kg")
                    denomL.remove("m")
                    numL.remove("s")
                    numL.remove("s")
                else:
                    cont = True
            if count > 0:
                print(numL)
                print(denomL)
                simplifiedN.extend(numL)
                simplifiedD.extend(denomL)
        except ValueError:
            pass






    print("NEW: The numerator is", simplifiedN, "and the denominator is", simplifiedD)
