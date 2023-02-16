# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:07:00 2023

@author: NickOne

"""


"""
                 Amaliyot shartlari
1. name degan ro`yxat yarating va kamida 3 ta yaqin do`stingizning ismini kiriting.
   Ro`yxatdagi har bir do`stingizngo qisqa xabar yozib konsolga chiqaring:
   
                 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                 \\\  Salom Ali ishlaring yaxshimi?               \\\
                 \\\  Husan va Hasan egizaklar                    \\\
                 \\\  G`ani g`ildirakni g`izzillatib g`ildiratdi  \\\
                 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
   
2. sonlar deb nomlangan ro`yxat yarating va ichiga turli sonlarni yuklang(musbat, manfiy, butun, o`nlik).
   Yuqoridagi ro`yxatdagi sonlar ustida turli arifmetik amallar bajarib ko`ring. Ro`yxatdagi ba`zi sonlarning qiymatini o`zgartiring, ba`zilarini esa almashtiring.
   
3. t_shaxslar va z_shaxslar degan 2 ta ro`yxat yarating va biriga o`zingiz eng ko`p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo`lgan shaxslarning ismini kiriting.
   Yuqoridagi ro`yxatlarning har biridan bittadan qiymatni sug`urib olib( .pop() ), quyidagi korinishda chiqaring:
       
                 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                 \\\  Men tarixiy shaxslardan Imom Buxoriy bilan,  \\\
                 \\\  zamonaviy shaxslardan esa Bill Gates bilan,  \\\
                 \\\  suhbat qilishni istar edim                   \\\
                 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                     
4. friends nomli bo`sh ro`yxat tuzing va unga .uppend() yordamida 5-6 ta mehmonga chaqirmoqchi bo`lgan do`stlaringizni kiriting.
   Yuqoridagi ro`yxatdan mexmonga kela olmaydigan odamlarni .remove() metodi yordamida o`chirib tashlang.
   Yangi mehmonlar deb nomlangan bo`sh ro`yxat yarating . .pop() va .append() metodlari yordamida mehmonga kelgan do`stlaringizning 
   ismini friends ro`yxatidan sug`urib olib, mehmonlar ro`yxatiga qo`shing.
   
"""


name = ['Shuhrat', 'Abror', 'Elmurod', 'Davron']    # keyingi qatordagi \n belgisi qator tashlash uchun ishlatiladi 
print("\n" + name[0] + " universitetni bu yil tamomladi va soxasi boyicha Dadasi " + name[3] + " ning oldida ish boshladi")
print("\n" + name[1] + " ning tug`ilgan kuniga " + name[2] + " bilan birgalikda sovg`a tayyorladik \n \n")


sonlar = [1, 23, -4, 2.5, -8.0, 9]
print(str(sonlar[1]) + " + " + str(sonlar[3]) + " = " + str(sonlar[1]+sonlar[3]) )
print(str(sonlar[4]) + " * " + str(sonlar[2]) + " = " + str(sonlar[4]*sonlar[2]) )
print(str(sonlar[1]) + " / " + str(sonlar[5]) + " = " + str(sonlar[1]/sonlar[5]) + "\n" )

sonlar[1] = sonlar[1]+sonlar[5]
sonlar[4] = sonlar[1]-sonlar[4]

print(str(sonlar[1]) + " + " + str(sonlar[3]) + " = " + str(sonlar[1]+sonlar[3]) )
print(str(sonlar[4]) + " * " + str(sonlar[2]) + " = " + str(sonlar[4]*sonlar[2]) )
print(str(sonlar[1]) + " / " + str(sonlar[5]) + " = " + str(sonlar[1]/sonlar[5]) + "\n" )


t_shaxslar = ["Albert Einstein", "Amur Temur", "Jules Verne"]
z_shaxslar = ["Devid Attenborough", "Elon Musk"]
print("Yoshligimizda " + t_shaxslar[2] + " asarlari orqali o`zga bir dunyolarni kashb qilar edik va aynan " + t_shaxslar.pop(2) + 
      " ning asarlari menda kitobga bo`lgan muhabbatning uyg`oniushiga sabab bo`lgan edi.")