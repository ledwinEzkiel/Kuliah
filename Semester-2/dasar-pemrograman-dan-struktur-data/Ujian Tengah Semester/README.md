# Ujian Tengah Semester

- Nama : Ledwin Ezkiel Wotulo
- NIM : 5720122028

### Soal

1. - Nama: Encong
   - Kuliah: STMIK Adhi Guna
   - Prodi: Sistem Informasi

   Buatlah program dengan output sebagai berikut (*gunakan variabel untuk menginisialisasi*)
   > Nama saya Encong kuliah di STMIK Adhi Guna program studi Sistem Informasi

2. Buatlah program dengan inputan
   a. Luas segitiga
   b. luas lingkaran dan keliling lingkaran
   c. Luas persegi panjang dan keliling persegi panjang

### Jawaban:

```PYTHON

# soal nomor 1
nama = 'Encong'
kuliah = 'STMIK Adhi Guna'
prodi = 'Sistem Informasi'

print("Nama saya", nama, "kuliah di", kuliah, "program studi", prodi)

# Soal nomor 2a

a = float(input('Masukan alas: '))
t = float(input('Masukan tinggi: '))
ls = 1/2 * a * t
print("Luas segitiga adalah", ls)

# Soal nomor 2b

jari_jari = float(input('Masukan jari-jari: '))
phi = 3.14
luas_lingkaran = phi * jari_jari * jari_jari
keliling_lingkaran = 2 * phi * jari_jari * jari_jari

print("Luas lingkaran adalah", luas_lingkaran)
print("keliling lingkaran adalah", keliling_lingkaran)

# Soal nomor 2c

panjang_pp = float(input('Masukan Panjang: '))
lebar_pp = float(input('Masukan Lebar: '))
luas_pp = 2 * (panjang_pp + lebar_pp)
keliling_pp = panjang * lebar

print("Luas pp adalah", luas_pp)
print("Keliling pp adalah", keliling_pp)
```