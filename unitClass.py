#!/usr/bin/python
_author_ = "Matthew Zheng"
_purpose_ = "Sets up the unit class"

class Unit:
    def __init__(self, unitName):
        self.unitName = unitName

    @classmethod
    def baseCheck(cls):
        #checks if it can be crossed out
