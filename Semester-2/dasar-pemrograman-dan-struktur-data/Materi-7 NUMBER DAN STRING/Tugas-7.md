# Tugas Praktikum 7

- Nama: Ledwin Ezkiel Wotulo
- NIM: 5720122028

## Pengantar

Number adalah tipe data Python yang menyimpan nilai numerik. Number adalah tipe data yang tidak berubah. Ini berarti, mengubah nilai dari sejumlah tipe data akan menghasilkan obejek baru yang dialokasikan.

## Tujuan dan Manfaat

- Dapat memahami konsep number, konversi dan bentuk dari string
- Dapat menulis sintak dasar number dan string

## Program

```python
# progam 1
a = "Hello World"

print("Karakter pada index ke-2:", a[2])
print("Karakter pada index ke-4:", a[4])
print("Karakter pada index ke-8:", a[4])
print("Karakter pada index ke-10:", a[9])

# program 2
a = "Hello World"

# Menampilkan karakter pada index ke 1 sampai 3
print(a[1:3])  # Output: el

# Menampilkan karakter pada index ke 2 sampai 5
print(a[2:6])  # Output: llo

# Menampilkan karakter pada index ke 7 sampai 11
print(a[6:10])  # Output: worl


# program 3

original_string = 'Hello , World'
print(original_string.lower())
print(original_string.upper())
kata = 'orang jahat adalah orang baik yang tersakiti'
x = kata.replace('a', 'i').replace('o', 'i').replace('e', 'i')
print(x)
```

## Analisis Program

Program 1
Program ini merupakan program sederhana yang menunjukkan cara mengakses karakter-karakter tertentu dari sebuah string di Python. Pada program ini, terdapat sebuah string yang diinisialisasi dengan nilai "Hello World", dan kemudian beberapa karakter pada indeks tertentu diambil dan ditampilkan di layar menggunakan perintah print(). Program ini akan menampilkan karakter-karakter pada indeks ke-2, ke-4, ke-8, dan ke-10 dari string "Hello World".

Program 2
Program ini merupakan program sederhana yang menunjukkan cara mengambil substring dari sebuah string di Python. Pada program ini, terdapat sebuah string yang diinisialisasi dengan nilai "Hello World", dan kemudian substring pada indeks tertentu diambil dan ditampilkan di layar menggunakan perintah print(). Program ini akan menampilkan substring yang dimulai dari indeks ke-1 sampai ke-3, indeks ke-2 sampai ke-5, dan indeks ke-7 sampai ke-11 dari string "Hello World".

Program 3
Program ini merupakan program sederhana yang menunjukkan cara mengubah huruf besar dan kecil serta mengganti beberapa karakter di dalam sebuah string di Python. Pada program ini, terdapat sebuah string yang diinisialisasi dengan nilai "Hello , World", dan kemudian string tersebut diubah menjadi huruf kecil dan huruf besar menggunakan method lower() dan upper(). Selain itu, terdapat sebuah variabel yang berisi string "orang jahat adalah orang baik yang tersakiti" yang diubah karakter-karakter tertentu menjadi karakter "i" menggunakan method replace(). Program ini akan menampilkan string "Hello , World" dalam huruf kecil dan huruf besar, serta string "iring jihit idil ihir bik yang tirsikiti" setelah diubah.