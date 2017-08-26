#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Get a user specified string of commonly used units and converts the product or remainder into another commonly used unit"

import math

def main():
    #determine which science-unit class to import
    mPorC = None
    while(mPorC != "math" and mPorC != "physics" and mPorC != "chemistry"):
        mPorC = input("Please type Math, Physics, or Chemistry to import the proper units for your question.\n").casefold()
    if(mPorC = "math"):
        import mathUnits
    elif(mPorC = "physics"):
        import physicsUnits
    elif(mPorC = "chemistry"):
        import chemistryUnits
    else:
        pass        

    #determine if we are multiplying or dividing units
    multiOrDiv = None
    while(multiOrDiv != "m" and multiOrDiv != "d"):
        multiOrDiv = input("Are you multiplying or dividing these units? Use m for multiply and d for divide.\n").casefold()
        print(multiOrDiv)

    if(multiOrDiv == "m"):
        #multiplication parsing
        pass

    elif(multiOrDiv == "d"):
        #division parsing
        pass

    else:
        print("it broke")


if __name__ == "__main__":
    main()