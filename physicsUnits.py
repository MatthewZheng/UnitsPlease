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

    #assignment and print values
    numL = prod.updatedNum
    denomL = prod.updatedDenom
    print("OLD: The numerator is", numL, "and the denominator is", denomL)


    #############Begin unit conversion cases####################################
    #Volt
    try:
        derivedN = ["m", "m", "kg"]
        derivedD = ["s", "s", "s", "A"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedN.append("V")
            numL.remove("m")
            numL.remove("m")
            numL.remove("kg")
            denomL.remove("s")
            denomL.remove("s")
            denomL.remove("s")
            denomL.remove("A")

    #wrong unit
    except ValueError:
        pass
    #check for inverse unit
    try:
        derivedN = ["s", "s", "s", "A"]
        derivedD = ["m", "m", "kg"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedD.append("V")
            denomL.remove("m")
            denomL.remove("m")
            denomL.remove("kg")
            numL.remove("s")
            numL.remove("s")
            numL.remove("s")
            numL.remove("A")
    #wrong unit
    except ValueError:
        pass

    #Coloumb
    try:
        derivedN = ["s", "A"]
        derivedD = []
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedN.append("C")
            numL.remove("s")
            numL.remove("A")
    except ValueError:
        pass
    try:
        derivedN = []
        derivedD = ["s", "A"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedD.append("C")
            denomL.remove("s")
            denomL.remove("A")
    except ValueError:
        pass

    #Watt
    try:
        derivedN = ["m", "m", "kg"]
        derivedD = ["s", "s", "s"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedN.append("W")
            numL.remove("kg")
            numL.remove("m")
            numL.remove("m")
            denomL.remove("s")
            denomL.remove("s")
            denomL.remove("s")
    except ValueError:
        pass
    try:
        derivedN = ["s", "s", "s"]
        derivedD = ["m", "m", "kg"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedD.append("W")
            numL.remove("s")
            numL.remove("s")
            numL.remove("s")
            denomL.remove("kg")
            denomL.remove("m")
            denomL.remove("m")
    except ValueError:
        pass

    #Joule
    try:
        derivedN = ["m", "m", "kg"]
        derivedD = ["s", "s"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedN.append("J")
            numL.remove("kg")
            numL.remove("m")
            numL.remove("m")
            denomL.remove("s")
            denomL.remove("s")
    except ValueError:
        pass
    try:
        derivedN = ["s", "s"]
        derivedD = ["m", "m", "kg"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedD.append("J")
            numL.remove("s")
            numL.remove("s")
            denomL.remove("kg")
            denomL.remove("m")
            denomL.remove("m")
    except ValueError:
        pass

    #Pascal
    try:
        derivedN = ["kg"]
        derivedD = ["m", "s", "s"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedN.append("Pa")
            numL.remove("kg")
            denomL.remove("m")
            denomL.remove("s")
            denomL.remove("s")
    except ValueError:
        pass
    try:
        derivedN = ["m", "s", "s"]
        derivedD = ["kg"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)
        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedD.append("Pa")
            numL.remove("m")
            numL.remove("s")
            numL.remove("s")
            denomL.remove("kg")
    except ValueError:
        pass


    #Newtons
    try:
        derivedN = ["kg", "m"]
        derivedD = ["s", "s"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)

        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedN.append("N")
            numL.remove("kg")
            numL.remove("m")
            denomL.remove("s")
            denomL.remove("s")
    except ValueError:
        pass
    try:
        derivedN = ["s", "s"]
        derivedD = ["kg", "m"]
        #check for membership in base dervied units
        for i in numL:
            if i in derivedN:
                derivedN.remove(i)
        for j in denomL:
            if j in derivedD:
                derivedD.remove(j)

        #check if a substitution of units can occur
        if (derivedN == [] and derivedD == []):
            simplifiedD.append("N")
            numL.remove("s")
            numL.remove("s")
            denomL.remove("kg")
            denomL.remove("m")
    except ValueError:
        pass
        

    #cancel out like units
    prod.cancel()

    #assignment
    simplifiedN.extend(numL)
    simplifiedD.extend(denomL)

    print("NEW: The numerator is", simplifiedN, "and the denominator is", simplifiedD)
