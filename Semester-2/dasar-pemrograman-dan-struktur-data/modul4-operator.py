import os
so = os.name
match so:
    case 'nt': os.system('cls')

# program 1 perhitungan sederhana
bilanganPertama = 15
bilanganKedua = 8
bilanganKetiga = 100

rumusPenjumlahan = bilanganPertama + bilanganKedua + bilanganKetiga
rumusPengurangan = bilanganPertama - bilanganKedua - bilanganKetiga
rumusPerkalian = bilanganPertama * bilanganKedua * bilanganKetiga
rumusPembagian = bilanganPertama / bilanganKedua / bilanganKetiga
rumusPangkat = bilanganPertama ** bilanganKedua

print(f"Penjumlahan = 15 + 8 + 100 = {rumusPenjumlahan}")
print(f"Penjumlahan = 15 - 8 - 100 = {rumusPengurangan}")
print(f"Penjumlahan = 15 * 8 * 100 = {rumusPerkalian}")
print(f"Penjumlahan = 15 / 8 / 100 = {rumusPembagian}")
print(f"Pangkat = 15 ** 8 = {rumusPangkat}")


# program 2 menghitung luas bangun datar

# 1 luas persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi

# 2 luas persegi panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp

# 3 luas segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5*alas_segitiga*tinggi_segitiga


# operator bitwise
a = 9
b = 4

print(f"a & b = {a & b}")
print(f"a | b = {a | b}")
print(f"~a = {~a}")
print(f"a ^ b = {a ^ b}")