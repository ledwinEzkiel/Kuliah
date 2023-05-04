# Pengulangan

Secara umum, pernyataan pada bahasa pemrograman akan dieksekusi secara berurutan. Pernyataan pertama dalam sebuah fungsi dijalankan pertama, diikuti oleh yang kedua, dan seterusnya. Tetapi akan ada situasi dimana Anda harus menulis banyak kode, dimana kode tersebut sangat banyak. Jika dilakukan secara manual maka Anda hanya akan membuang-buang tenaga dengan menulis beratus-ratus bahkan beribu-ribu kode. Untuk itu Anda perlu menggunakan pengulangan di dalam bahasa pemrograman Python.

Di dalam bahasa pemrograman Python pengulangan dibagi menjadi 3 bagian, yaitu :

- While Loop
- For Loop
- Nested Loop

## While Loop

Pengulangan `While Loop` di dalam bahasa pemrograman Python dieksesusi statement berkali-kali selama kondisi bernilai benar atau `True`.

Dibawah ini adalah contoh penggunaan pengulangan `While Loop`:

```python
#Contoh penggunaan While Loop

count = 0
while (count < 9):
    print ("The count is: ", count)
    count = count + 1

print ("Good bye!")
```

```output
The count is:  0
The count is:  1
The count is:  2
The count is:  3
The count is:  4
The count is:  5
The count is:  6
The count is:  7
The count is:  8
Good bye!
```

```python
x = "INFORMASI"
while x:
    print(x, " ")
    x = x[1:]
```

```output
INFORMASI  
NFORMASI  
FORMASI  
ORMASI  
RMASI  
MASI  
ASI  
SI  
I
```

## For Loop
Pengulangan `for` pada Python memiliki kemampuan untuk mengulangi item dari urutan apapun, seperti `list` atau `string`.

Dibawah ini adalah contoh penggunaan pengulangan For Loop.

```PYTHON
# Contoh pengulangan for sederhana

angka = [1,2,3,4,5]
for x in angka:
    print(x)

# Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print ("Saya suka makan", makanan)
```
```OUTPUT
1
2
3
4
5
Saya suka makan nanas
Saya suka makan apel
Saya suka makan jeruk
```
