from datetime import datetime
import os
os.system ("cls")

hozir = datetime.now()

mustaqillik = datetime(hozir.year, 9, 1)

farq = mustaqillik - hozir

print("Mustaqillik bayramiga:", farq.days, "kun qoldi")