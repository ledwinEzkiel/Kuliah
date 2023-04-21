# Penerapan Konsep Tipe Data

## Tipe data
Tipe data adalah suatu media atau memori pada komputer yang digunakan untuk menampung informasi. Python sendiri mempunyai tipe data yang cukup unik bila kita bandingkan dengan bahasa pemrograman yang lain. Berikut adalah tipe data dari bahasa pemrograman Python

- String
- Integer
- Float
- Boolean
- List
- Tuple
- Dictionary
- Complex

```python

#tipe data Boolean
print(True)

#tipe data String
print("string dengan menggunakan tanda kutip dua")
print('ini string menggunakan tanda kutip satu')
#tipe data string dengan menjelaskan spesial karakter atau escape sequences
print('ini adalah tanda single quote (\')')
print("ini adalah tanda double quote (\")")
print("ini adalah tanda slash (\\)")
print("Algoritma\nPemrograman") #menggunakan \n
print("Algoritma\bPemrograman") #menggunakan \b
print("Algoritma\tPemrograman") #menggunakan \t
print("Algoritma\rPemrograman") #menggunakan \b

#tipe data Integer
print(20)

#tipe data Float
print(3.14)
print(.2)
print(4.2e-3)

#tipe data Binary
print(0b10)

#tipe data octal
print(0o10)

#tipe data Hexadecimal
print('tipe data heksa desimal',0x10)

#tipe data Complex
print(5j)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Budi", 'umur':20})
#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Budi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
print(type(biodata)) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary

```

```
output:

True
string dengan menggunakan tanda kutip dua
ini string menggunakan tanda kutip satu
ini adalah tanda single quote (')
ini adalah tanda double quote (")
ini adalah tanda slash (\)
Algoritma
Pemrograman
AlgoritmaPemrograman
Algoritma	Pemrograman
Pemrograman
20
3.14
0.2
0.0042
2
8
tipe data heksa desimal 16
5j
[1, 2, 3, 4, 5]
['satu', 'dua', 'tiga']
(1, 2, 3, 4, 5)
('satu', 'dua', 'tiga')
{'nama': 'Budi', 'umur': 20}
{'nama': 'Budi', 'umur': 21}
<class 'dict'>

```
