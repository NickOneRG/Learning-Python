# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:37:05 2023

@author: NickOne
"""

son1, son2 = int(input("\n Son kiriting\n\n>>>  ")), int(input("\n Yana bir son kiriting\n\n>>>  "))


javoby = son1 + son2
javoba = son1 - son2
javobk = son1 * son2
javobb = son1 / son2


print("\nSiz kiritgan \n\n" + "            " + str(son1) + " + " + str(son2) + " = " + str(javoby) + "\n"
      + "            " + str(son1) + " - " + str(son2) + " = " + str(javoba) + "\n"
      + "            " + str(son1) + " * " + str(son2) + " = " + str(javobk) + "\n"
      + "            " + str(son1) + " / " + str(son2) + " = " + str(javobb) + "\n")