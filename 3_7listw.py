# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:51:06 2023

@author: NickOne
"""

"""
        Ro`yxatlar bilan ishlash 
    Ro`yxatni tartiblash
Aksar hollarda ro`yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin.
Buning uchun maxsus .sort() metodidan foydalanamiz.
"""

cars = ['bmw', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)     # Tartiblashda bosh xariflar kichik xariflardan avval kelishini hisobga oling . Agar ro`yxatda so`zlarning birinchi harfi katta-kichik aralash yozilgan bo`lsa, ularni bir ko`rinishga keltirib olish maqsadga muvofiq bo`ladi.

cars.append('MAN')

cars.sort()
print(cars)

# Yuqoridagi misolda MAN elementi bosh harf bilan boshlangani uchun ro`yxatning boshidan joy oldi.
# Ro`yxatni teskari tartiblash uchun .sort() metodi ichida reverse=True argumentini yozamiz.

cars.sort(reverse=True)
print(cars)