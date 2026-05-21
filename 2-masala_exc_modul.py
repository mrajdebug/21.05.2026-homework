from datetime import datetime
import os
os.system ("cls")

yil = int(input("Tug`ilgan yilingizni kiriting: "))
oy = int(input("Tug`ilgan oyingizni kiriting: "))
kun = int(input("Tug`ilgan kuningizni kiriting: "))

hozir = datetime.now()
# print(hozir.year, hozir.month, hozir.day)

tugilgan_sana = datetime(yil, oy, kun)

farq = hozir - tugilgan_sana
print("Siz tug'ilganingizga:", farq.days, "kun bo'ldi")

