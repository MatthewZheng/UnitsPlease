#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Get a user specified string of commonly used units and converts the product or remainder into another commonly used unit"

from productClass import Product

def main():
    #determine if we are multiplying or dividing units
    multiOrDiv = None
    while(multiOrDiv != "m" and multiOrDiv != "d"):
        multiOrDiv = input("Are you multiplying or dividing these units? Use m for multiply and d for divide.\n").casefold()
        rawStrNum = input("Please type out all the units in your reactant/equation's numerator. If you have any negative powers, please convert them to division and use the division option. Format your input with commas. Ex: m, s, kg, etc\n")
        numL = [x.strip() for x in rawStrNum.split(',')]

    if(multiOrDiv == "m"):
        #multiplication parsing
        parseMulti = Product(numL, [])

    elif(multiOrDiv == "d"):
        #division parsing
        rawStrDenom = input("Please type out all the units in your reactant/equation's denominator. If you have any negative powers, please put them in the numerator. If you have powers, use a carat to denote where the power starts. Format your input with commas. Ex: m, s^2, kg, etc.\n")
        denomL = [x.strip() for x in rawStrDenom.split(',')]
        parseDiv = Product(numL, denomL)
    else:
        print("it broke")


    #determine which science-unit class to import
    mPorC = None
    while(mPorC != "both" and mPorC != "physics" and mPorC != "chemistry"):
        mPorC = input("Please type Physics, Chemistry or Both to try to simplify the units into proper units for your question.\n").casefold()

    if(mPorC == "both"):
        import physicsUnits
        import chemistryUnits

    elif(mPorC == "physics"):
        import physicsUnits

    elif(mPorC == "chemistry"):
        import chemistryUnits

    else:
        print("Oops, something went wrong with your imports. Check that chemistryUnits.py and physicsUnits.py exists.")

    if(multiOrDiv == "m"):
        try:
            chemistryUnits.tryAll(parseMulti)
        except NameError:
            print("Note to user -- you chose not to import chemistry units.")
        try:
            physicsUnits.tryAll(parseMulti)
        except NameError:
            print("Note to user -- you chose not to import physics units.")

    elif(multiOrDiv == "d"):
        try:
            chemistryUnits.tryAll(parseDiv)
        except NameError:
            print("Note to user -- you chose not to import chemistry units.")
        try:
            physicsUnits.tryAll(parseDiv)
        except NameError:
            print("Note to user -- you chose not to import physics units.")
    else:
        print("it broke dhude")


if __name__ == "__main__":
    main()
