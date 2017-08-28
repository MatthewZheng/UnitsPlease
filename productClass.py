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

    def convertNum(self):
        '''Converts all numerators into base units'''
        self.updatedNum = (super().baseCheck(self.numerator))
        # return(self.updatedNum)

    def convertDenom(self):
        '''Converts all denominators into base units'''
        self.updatedDenom = (super().baseCheck(self.denominator))
        # return(self.updatedDenom)

    def derivedToBase(self):
        '''This will convert any derived units such as N (newtons), T (teslas), etc to their respective base units. Output: ([num], [denom])'''
        numL = self.updatedNum
        denomL = self.updatedDenom

        # if(all(x in [numL] for x in ["kg", "m"]) and (all(y in [denomL] for y in ["s", "s"]))):
        #     numL.remove("kg", "m")
        #     denomL.remove("s", "s")
        #     numL.append("N")

        #Pascal
        try:
            #Swap all instances of derived unit
            for i in range(numL.count("Pa")):
                if("Pa" in numL):
                    numL.remove("Pa")
                    numL.extend(["N"])
                    denomL.extend(["m", "m"])
        #Unit not found
        except NameError:
            pass
        try:
            for i in range(denomL.count("Pa")):
                if("Pa" in denomL):
                    denomL.remove("Pa")
                    denomL.extend(["N"])
                    numL.extend(["m", "m"])
        except NameError:
            pass

        #Farad
        try:
            for i in range(numL.count("F")):
                if("F" in numL):
                    numL.remove("F")
                    numL.extend(["C"])
                    denomL.extend(["V"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("F")):
                if("F" in denomL):
                    denomL.remove("F")
                    denomL.extend(["C"])
                    numL.extend(["V"])
        except NameError:
            pass

        #Ohm
        try:
            for i in range(numL.count("ohm")):
                if("ohm" in numL):
                    numL.remove("ohm")
                    numL.extend(["V"])
                    denomL.extend(["A"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("ohm")):
                if("ohm" in denomL):
                    denomL.remove("ohm")
                    denomL.extend(["V"])
                    numL.extend(["A"])
        except NameError:
            pass

        #Siemens
        try:
            for i in range(numL.count("S")):
                if("S" in numL):
                    numL.remove("S")
                    numL.extend(["A"])
                    denomL.extend(["V"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("S")):
                if("S" in denomL):
                    denomL.remove("S")
                    denomL.extend(["A"])
                    numL.extend(["V"])
        except NameError:
            pass

        #Tesla
        try:
            for i in range(numL.count("T")):
                if("T" in numL):
                    numL.remove("T")
                    numL.extend(["Wb"])
                    denomL.extend(["m", "m"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("T")):
                if("T" in denomL):
                    denomL.remove("T")
                    denomL.extend(["Wb"])
                    numL.extend(["m", "m"])
        except NameError:
            pass

        #Henry
        try:
            for i in range(numL.count("H")):
                if("H" in numL):
                    numL.remove("H")
                    numL.extend(["Wb"])
                    denomL.extend(["A"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("H")):
                if("H" in denomL):
                    denomL.remove("H")
                    denomL.extend(["Wb"])
                    numL.extend(["A"])
        except NameError:
            pass

        #Lux
        try:
            for i in range(numL.count("lx")):
                if("lx" in numL):
                    numL.remove("lx")
                    numL.extend(["lm"])
                    denomL.extend(["m","m"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("lx")):
                if("lx" in denomL):
                    denomL.remove("lx")
                    denomL.extend(["lm"])
                    numL.extend(["m", "m"])
        except NameError:
            pass

        #Gray
        try:
            for i in range(numL.count("Gy")):
                if("Gy" in numL):
                    numL.remove("Gy")
                    numL.extend(["J"])
                    denomL.extend(["kg"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("Gy")):
                if("Gy" in denomL):
                    denomL.remove("Gy")
                    denomL.extend(["J"])
                    numL.extend(["kg"])
        except NameError:
            pass

        #Sievert
        try:
            for i in range(numL.count("Sv")):
                if("Sv" in numL):
                    numL.remove("Sv")
                    numL.extend(["J"])
                    denomL.extend(["kg"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("Sv")):
                if("Sv" in denomL):
                    denomL.remove("Sv")
                    denomL.extend(["J"])
                    numL.extend(["kg"])
        except NameError:
            pass

        ######################SPECIAL CASES####################
        #Celcius
        try:
            for i in range(numL.count("°C")):
                if("°C" in numL):
                    numL.remove("°C")
                    numL.extend(["K"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("°C")):
                if("°C" in denomL):
                    denomL.remove("°C")
                    denomL.extend(["K"])
        except NameError:
            pass

        #Hertz
        try:
            for i in range(numL.count("Hz")):
                if("Hz" in numL):
                    numL.remove("Hz")
                    denomL.extend(["s"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("Hz")):
                if("Hz" in denomL):
                    denomL.remove("Hz")
                    numL.extend(["s"])
        except NameError:
            pass

        #Becquerel
        try:
            for i in range(numL.count("Bq")):
                if("Bq" in numL):
                    numL.remove("Bq")
                    denomL.extend(["s"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("Bq")):
                if("Bq" in denomL):
                    denomL.remove("Bq")
                    numL.extend(["s"])
        except NameError:
            pass
        ########################################################


        #DO NOT CHANGE THE POSITION OF VARIABLES:
        #Newtons
        try:
            for i in range(numL.count("N")):
                if("N" in numL):
                    numL.remove("N")
                    numL.extend(["kg", "m"])
                    denomL.extend(["s", "s"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("N")):
                if("N" in denomL):
                    denomL.remove("N")
                    denomL.extend(["kg", "m"])
                    numL.extend(["s", "s"])
        except NameError:
            pass

        #Joules
        try:
            for i in range(numL.count("J")):
                if("J" in numL):
                    numL.remove("J")
                    numL.extend(["m", "m", "kg"])
                    denomL.extend(["s", "s"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("J")):
                if("J" in denomL):
                    denomL.remove("J")
                    denomL.extend(["m", "m", "kg"])
                    numL.extend(["s", "s"])
        except NameError:
            pass

        #Volts
        try:
            for i in range(numL.count("V")):
                if("V" in numL):
                    numL.remove("V")
                    numL.extend(["m", "m", "kg"])
                    denomL.extend(["s", "s", "s", "A"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("V")):
                if("V" in denomL):
                    denomL.remove("V")
                    denomL.extend(["m", "m", "kg"])
                    numL.extend(["s", "s", "s", "A"])
        except NameError:
            pass

        #Webers
        try:
            for i in range(numL.count("Wb")):
                if("Wb" in numL):
                    numL.remove("Wb")
                    numL.extend(["m", "m", "kg"])
                    denomL.extend(["s", "s", "A"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("Wb")):
                if("Wb" in denomL):
                    denomL.remove("Wb")
                    denomL.extend(["m", "m", "kg"])
                    numL.extend(["s", "s", "A"])
        except NameError:
            pass

        #Watts
        try:
            for i in range(numL.count("W")):
                if("W" in numL):
                    numL.remove("W")
                    numL.extend(["m", "m", "kg"])
                    denomL.extend(["s", "s"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("W")):
                if("W" in denomL):
                    denomL.remove("W")
                    denomL.extend(["m", "m", "kg"])
                    numL.extend(["s", "s"])
        except NameError:
            pass

        #Lumen
        try:
            for i in range(numL.count("lm")):
                if("lm" in numL):
                    numL.remove("lm")
                    numL.extend(["cd"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("lm")):
                if("lm" in denomL):
                    denomL.remove("lm")
                    denomL.extend(["cd"])
        except NameError:
            pass

        #Coloumb
        try:
            for i in range(numL.count("C")):
                if("C" in numL):
                    numL.remove("C")
                    numL.extend(["s", "A"])
        except NameError:
            pass
        try:
            for i in range(denomL.count("C")):
                if("C" in denomL):
                    denomL.remove("C")
                    denomL.extend(["s", "A"])
        except NameError:
            pass


        self.updatedNum = numL
        self.updatedDenom = denomL
