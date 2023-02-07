# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:34:48 2023

@author: NickOne
"""

name = input("What is your name?\n>>>")
age = int(input("How old are you?\n>>>"))

print(f"Hi!, {name.title()}")

if 18 < age:
    print("Ok!")   
else:    
    print("You are under age")
    
    
bday = int(input("what is your birth day\n>>>"))
tday = 2023
xday = tday - bday

if xday > 18:
    print("You are good to go")
else:
    print("Please wait until you 18+")