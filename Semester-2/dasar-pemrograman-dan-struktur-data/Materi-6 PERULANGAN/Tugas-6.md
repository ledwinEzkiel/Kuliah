# Tugas Praktikum 6

- Nama: Ledwin Ezkiel Wotulo
- NIM: 5720122028

## Pengantar

Apa itu program perulangan?
Perulangan adalah sebuah kondisi dimana satu atau beberapa baris kode program di eksekusi secara berulang-ulang. Loop digunakan untuk mengeksekusi blok kode yang sama berulang kali, blok kode yang sama dijalankan berulang-ulang beberapa kali selama kondisi tertentu benar.

## Tujuan dan Manfaat

- Dapat mengerti dan memahami konsep dasar perulangan
- Dapat memahami sintaks perulangan

## Program

```python
# program 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
genap = 0
ganjil = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    i += 1

print("List angka:", numbers)
print("Jumlah bilangan genap:", genap)
print("Jumlah bilangan ganjil:", ganjil)


# program 2
number = int(input("Masukan angka: "))
for i in range(1, 11):
    print(number, "*", i, "=", number*i)

# program 3
n = 11
a, b = 0, 1

for i in range(n):
    print(b, end=" ")
    a, b = b, a + b
```

## Analisis Program

Program 1:
Program ini menghitung jumlah bilangan genap dan ganjil dari sebuah list angka menggunakan loop while dan conditional statement if else. Variabel genap dan ganjil diinisialisasi dengan nilai awal 0, dan kemudian loop while akan berjalan selama nilai i kurang dari panjang list angka. Pada setiap iterasi, nilai indeks ke-i dari list akan diperiksa apakah merupakan bilangan genap atau ganjil. Jika genap, variabel genap akan ditambah 1. Jika ganjil, variabel ganjil akan ditambah 1. Setelah loop selesai, jumlah bilangan genap dan ganjil akan dicetak. Program ini dapat dijadikan referensi dalam memahami loop while dan penggunaan conditional statement pada Python.

Program 2:
Program ini meminta pengguna untuk memasukkan sebuah angka dan kemudian mencetak tabel perkalian dari angka tersebut, mulai dari 1 hingga 10. Program ini menggunakan loop for untuk mengulang sebanyak 10 kali. Pada setiap iterasi, nilai variabel i akan berubah dari 1 hingga 10 dan hasil perkalian antara angka yang dimasukkan oleh pengguna dan variabel i akan dicetak. Program ini dapat digunakan untuk mempelajari cara menggunakan loop for dan menerima input dari pengguna pada Python.

Program 3:
Program ini mencetak deret bilangan Fibonacci dengan panjang n. Program ini menggunakan loop for dan dua variabel a dan b. Pada awalnya, variabel a diinisialisasi dengan nilai 0 dan variabel b diinisialisasi dengan nilai 1. Selama loop berjalan, nilai variabel a akan berganti dengan nilai variabel b, dan nilai variabel b akan berganti dengan jumlah variabel a dan b. Program ini mencetak nilai variabel b pada setiap iterasi loop. Program ini dapat digunakan sebagai referensi dalam mempelajari loop for dan cara menghasilkan deret bilangan Fibonacci pada Python.