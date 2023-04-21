import os
so = os.name
match so:
    case "nt": os.system('cls')

# variabel da tipe data
print("Variable dan Tipe Data")
print(False)
print(type(False))
print("Ini adalah Tulisan Berupa String")
print(100)
print(1e-3)
print("Bilangan Hexadesimal dari 0x01 adalah", 0x01)
print(10)
print(type(2+6j))
print(2+6j)
print(type(2+6j))
print([96, 97, 98, 99, 100])
print(['seratus', 'duaratus', 'tigaratus'])
print({'nama': 'ani', 'umur': 19})
print("This string contains a single quote (\') character\n")

# nomor 2
"""
Tipe data Boolean
simpan dengan nama boolean.py
"""

narkoba = False
belajar = True

print(narkoba)
print(belajar)

"""
Tipe data String
simpan dengan nama string.py
"""

first_name = "Ledwin"
middle_name = "Ezkiel"
last_name = "Wotulo"

sapa = f"Halo {first_name} {middle_name} {last_name}"
print(sapa)

z = 1+5j
print(z)
print(type(z))
