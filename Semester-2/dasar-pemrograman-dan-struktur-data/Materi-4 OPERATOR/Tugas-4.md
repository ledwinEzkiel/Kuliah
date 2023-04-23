# Tugas Praktikum 4

- Nama: Ledwin Ezkiel Wotulo
- NIM : 5720122028

## Pengantar

Operator adalah symbol yang biasa dilibatkan dalam program untuk melakukan sesuatu operasi atau manipulasi, sebagai contoh yang dapat diimplementasikan menggunakan operator, `5 + 10 = 15`, Dimana `5` dan `10` adalah operan dan `+` adalah operator.

## Tujuan dan Manfaat

- Dapat memahami konsep dasar operator

## program

```python
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
print(f"luas persegi adalah {luas_persegi}")

# 2 luas persegi panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp
print(f"luas persegi panjang adalah {luas_pp}")

# 3 luas segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
print(f"luas segitiga adalah {luas_segitiga}")


# operator bitwise
a = 9
b = 4

print(f"a & b = {a & b}")
print(f"a | b = {a | b}")
print(f"~a = {~a}")
print(f"a ^ b = {a ^ b}")
```

## Analisis Program

Program pertama adalah program perhitungan sederhana yang menggunakan operator aritmatika untuk melakukan operasi penjumlahan, pengurangan, perkalian, pembagian, dan pemangkatan. Nilai-nilai bilangan yang digunakan sudah didefinisikan sebelumnya. Program menggunakan fungsi `print()` untuk menampilkan hasil operasi aritmatika.

Program kedua adalah program untuk menghitung luas bangun datar, yaitu persegi, persegi panjang, dan segitiga. Setiap bangun datar didefinisikan menggunakan variabel-variabel tertentu seperti panjang sisi, panjang dan lebar, serta alas dan tinggi. Setelah itu, program menggunakan operator aritmatika untuk menghitung luas masing-masing bangun datar dan menampilkannya pada layar menggunakan `print()`.

Program terakhir adalah program operator bitwise yang menggunakan operator bitwise and `(&)`, or `(|)`, negasi/not `(~)`, dan xor `(^)`. Program menggunakan fungsi `print()` untuk menampilkan hasil operasi bitwise pada layar.
