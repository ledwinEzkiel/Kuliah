import os
so = os.name
match so:
    case 'nt': os.system('cls')


# Program 1 - Mengecek jenis segitiga

a = 5
b = 3
c = 2

if(a == b == c):
    print("Segitiga sama sisi")
elif(a == b != c):
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")

# program 2 

x = 2020

if(x % 4 == 0):
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")


# Program untuk mendeteksi zodiak/astrologi Cina dari tahun lahir

# Definisikan variabel tahun lahir
tahun_lahir = 2028

# Hitung zodiak Cina berdasarkan tahun lahir
if (tahun_lahir - 1900) % 12 == 0:
    zodiak = 'Monyet'
elif (tahun_lahir - 1900) % 12 == 1:
    zodiak = 'Ayam'
elif (tahun_lahir - 1900) % 12 == 2:
    zodiak = 'Anjing'
elif (tahun_lahir - 1900) % 12 == 3:
    zodiak = 'Babi'
elif (tahun_lahir - 1900) % 12 == 4:
    zodiak = 'Tikus'
elif (tahun_lahir - 1900) % 12 == 5:
    zodiak = 'Banteng'
elif (tahun_lahir - 1900) % 12 == 6:
    zodiak = 'Macan'
elif (tahun_lahir - 1900) % 12 == 7:
    zodiak = 'Kelinci'
elif (tahun_lahir - 1900) % 12 == 8:
    zodiak = 'Naga'
elif (tahun_lahir - 1900) % 12 == 9:
    zodiak = 'Ular'
elif (tahun_lahir - 1900) % 12 == 10:
    zodiak = 'Kuda'
else:
    zodiak = 'Domba'

print("Zodiak cina")
print("Tahun lahir anda", tahun_lahir)
print("Zodiak cina", zodiak)


# Program untuk mendeteksi zodiak/astrologi Yunani dari tanggal dan bulan lahir

# Meminta input tanggal dan bulan lahir dari pengguna
tanggal = int(input("Masukkan tanggal lahir Anda: "))
bulan = int(input("Masukkan bulan lahir Anda (dalam angka, contoh: Januari = 1): "))

# Menggunakan kondisi if untuk mendeteksi zodiak Yunani berdasarkan tanggal dan bulan lahir
if (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
    zodiak = 'Aquarius'
elif (bulan == 2 and tanggal >= 19) or (bulan == 3 and tanggal <= 20):
    zodiak = 'Pisces'
elif (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
    zodiak = 'Aries'
elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
    zodiak = 'Taurus'
elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
    zodiak = 'Gemini'
elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
    zodiak = 'Cancer'
elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
    zodiak = 'Leo'
elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
    zodiak = 'Virgo'
elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
    zodiak = 'Libra'
elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
    zodiak = 'Scorpio'
elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
    zodiak = 'Sagittarius'
else:
    zodiak = 'Capricorn'

# Menampilkan hasil
print("Zodiak/astrologi Yunani dari tanggal lahir Anda adalah:", zodiak)
