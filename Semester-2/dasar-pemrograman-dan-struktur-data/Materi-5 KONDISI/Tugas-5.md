# Tugas Praktikum 5

- Nama: Ledwin Ezkiel Wotulo
- NIM : 5720122028

## Pengantar

Pengmabilan keputusan (kodisi if) digunakan untuk mengantisipasi kondisi yang terjadi saat jalannya program dan menentukan tindakan apa yang diambil sesuai dengan kondisi.

## Tujuan dan Manfaat
- Dapat mengerti konsep setiap perkondisian, seperti if..else..elif
- Dapat mengerti dasar sintaks kondisi

## Program

```python
# program 1
x = 2
y = 4
z = 8

if(x == y == z):
    print("Segitiga Sama sisi")
elif(x == y != z):
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")

# program 2
tahun = 2022

if(tahun % 4 == 0):
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")

tahun_lahir = 2028

# Program 3
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


# Program 4
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
```

## Analisis Program


Program 1 adalah program untuk menentukan jenis segitiga berdasarkan panjang sisi-sisinya. Program ini menginisialisasi variabel x, y, dan z dengan bilangan bulat. Kemudian, program mengevaluasi apakah segitiga tersebut sama sisi, sama kaki, atau sembarang. Jika x sama dengan y sama dengan z, maka segitiga tersebut sama sisi, jika x sama dengan y tetapi tidak sama dengan z, maka segitiga tersebut sama kaki, dan jika semua sisi tidak sama, maka segitiga tersebut sembarang. Program ini menggunakan struktur percabangan if-elif-else untuk mengevaluasi kondisi dan mencetak hasilnya.

Program 2 adalah program untuk menentukan apakah sebuah tahun adalah tahun kabisat atau tidak. Program ini menginisialisasi variabel tahun dengan bilangan bulat. Kemudian, program mengevaluasi apakah tahun tersebut dapat dibagi habis dengan 4. Jika dapat dibagi habis dengan 4, maka tahun tersebut adalah tahun kabisat, jika tidak, maka tahun tersebut bukan tahun kabisat. Program ini menggunakan struktur percabangan if-else untuk mengevaluasi kondisi dan mencetak hasilnya.

Program 3 adalah program untuk menentukan zodiak Cina berdasarkan tahun lahir seseorang. Program ini menginisialisasi variabel tahun_lahir dengan bilangan bulat. Kemudian, program menggunakan operasi modulo untuk menentukan sisa hasil pembagian tahun_lahir dengan 12. Setiap sisa hasil pembagian mewakili sebuah zodiak Cina. Program ini menggunakan struktur percabangan if-elif-else untuk mengevaluasi kondisi dan mencetak hasilnya.

Program 4 adalah program untuk menentukan zodiak Yunani berdasarkan tanggal dan bulan lahir seseorang. Program ini mengambil input dari pengguna berupa tanggal dan bulan lahir. Kemudian, program menggunakan struktur percabangan if-elif-else untuk mengevaluasi tanggal dan bulan lahir dan menentukan zodiak Yunani yang sesuai. Program ini mencetak zodiak Yunani yang sesuai.

Kesimpulannya, keempat program tersebut menggunakan struktur percabangan if-elif-else dan operasi matematika sederhana untuk mengevaluasi kondisi tertentu dan memberikan hasil yang sesuai berdasarkan input yang diberikan. Semua program tersebut relatif sederhana dan digunakan untuk tujuan yang berbeda-beda.