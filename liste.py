# -*- coding: utf-8 -*-
"""
Created on Wed Feb  10 13:16:06 2023

@author: NickOne
"""

mevalar = ['olma', 'anjir', 'shaftoli', 'o`rik']
narxlar = [12000, 18000, 10900, 22000]
sonlar = [10, 12, 345, -23, 445, 61,-45, 56, -34]

print("\n")

print("Birinchi mevalar: ", mevalar[0] +" "+ mevalar[1] +" "+ mevalar[2].title() +" "+ mevalar[3].upper() +"\n")


print(narxlar[2] + narxlar[3] )


print(sonlar[-1])
print("\n")


"""
Yangi element qo`shish

Ro`yxatga yangi element qo`shishning ikki yo`li bor, quyida ular bilan tanishamiz.

Birinchi usul: .append() metodi yordamida ro`yhatning oxiriga qiymat qo`shish:
"""

mevalar.append("tarvuz")  # mevalarga tarvuz qo`shamiz
print(mevalar)            # append() meto`di bo`sh ro`yxatni to`ldirishda juda qulay. Odatda, dastur boshida bo`sh ro`yxat yaratilib, dastur davomida ro`yxat foydalanuvchi tomonidan to`ldirib borilishi odatiy hol.

print("\n")
"""
Ro`yxatning istalgan joyiga yangi element qo`shish uchun .insert() metodidan foydalanamiz.
 .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:
""" 

cars = ['Lasetti', 'Nexia 3','Cobalt']
print(cars)

cars.insert(0, 'Malibu')
print(cars)

cars.insert(2, "Damas")
print(cars)

print("\n")

"""
     Elementni o`chirish
Ro`yxatni biror elementni olib tashlash uchun uning indeksi yoki qiymatini bilishimiz lozim.

Elementni indeksi yordamida ilib tashlash uchun del operatoridan foydalanamiz: 
"""

del mevalar[1]      # 2-element (anjir) ni o`chirib tashlaymiz.
print(mevalar)