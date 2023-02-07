# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:57:34 2023

@author: NickOne
"""

#   3.3 Matnlar bilan ishlash
#    upper(), lower(), title() va capitalize() metodlari

name = 'shohjaxon'
fname = 'sharobidinov'

name_fname = f"{name} {fname}"
 
 
print(name_fname.upper())       # upper() metodi matindagi har bir harifni bosh harifga o`zgartiradi.
print(name_fname.lower())       # lower() metodi har bir harifni kichik harfga o`zgartiradi.
print(name_fname.title())       # title() metodi matindagi harbir so`zning birinchi harfini katta bilan yozadi.
print(name_fname.capitalize())  # capitalize() esa matndagi birinchi so`zning birinchi harfini katta bilan yozadi.

print("\n")

#    strip(), rstrip() va lstrip() metodlari
#    Bu metodlar matinning boshi va oxiridagi bo`sh joylarni olib tashlaydi.

meva = "     olma    "

print("Men " + meva.lstrip() + " yaxshi ko`raman")  # lstrip() matn boshidagi bo`shliqni
print("Men " + meva.rstrip() + " yaxshi ko`raman")  # rstrip() matn oxiridagi bo`shliqni,
print("Men " + meva.strip() + " yaxshi ko`raman")   # strip() matn boshi va oxiridagi bo`shliqlarni olib tashlaydi.

print("\n")

"""
Yuqoridagi metodlar o`zgaruvchi ichidagi asl matnni o`zgartirmaydi!
O`zgartirilgan matinni saqlab qolish uchun uni qaytadan o`zgaruvchiga yuklash lozim:
    meva = meva.strip()
"""

print("Men " + meva + " yaxshi ko`raman")
meva = meva.strip()
print("Men " + meva + " yaxshi ko`raman")

# matinlar bilan ishlaydigan metodlar: www.w3schools.com/python/python_ref_string.asp