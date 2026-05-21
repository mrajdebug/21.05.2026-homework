from translate import Translator
import os
os.system ("cls")


list1 = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]

tarjimon = Translator(to_lang = "en")

# natija = tarjimon.translate(list1)
# print(natija)

dict = {}

for i in list1:
    if type(i) == str:
        natija = tarjimon.translate(i)
        dict[i] = natija

    else:
        dict[i] = i

print(dict)
