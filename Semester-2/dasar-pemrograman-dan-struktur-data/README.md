
# Dasar Pemrograman & Struktur Data

Semua file ini merupakan bahasa pemrograman Python


## Syntax dasar pada Python
### Pendahuluan
Algoritma adalah urutan aksi-aksi yang dinyatakan dengan jelas dan tidak rancu untuk memecahkan suatu masalah dalam rentang waktu tertentu. Setiap aksi harus dapat dikerjakan dan mempunyai efek tertentu.

Algoritma dapat dituliskan dengan banyak cara, mulai dari menggunakan bahasa alami yang digunakan sehari-hari, simbol grafik bagan alir, sampai menggunakan bahasa pemograman seperti bahasa Python

### Syntax dasar
`print()` merupakan salah satu fungsi dari python untuk mencetak, dengan meletakkan kurung buka dan kurung tutup, untuk di Python versi 2.x tidak perlu menggunakan kurung buka dan tutup atau kurung kurawal (), cukup dipisahkan dengan spasi.

Python 3.x, memiliki perbedaan dengan python 2.x dalam mencetakan tipe data string secara langsung, dengan memasukkan ke dalam kutip atau tanda petik terlebih dahulu.

```python
print("Hello World") #menggunakan tanda petik dua
print('Hello World') #menggunakan tanda petik tunggal

```
```
output:
Hello World
Hello World
```


### Case Sensitivity
bahasa pemrograman python bersifat case sensitive, yang artinya huruf besar dan huruf kecil memiliki perbedaan. sebagai contoh seperti pada contoh program di atas,menggunakan `print()` akan langsung menampilkan output nya, selanjutnya jika menggunakan `Print()`, `PRINT()`, `PrInT()` atau fungsi tidak lengkap seperti `prnt()` akan muncul pesan error.

NOTE: perlu diperhatikan, case sensitive juga berlaku untuk function lainnya.


### Komentar pada Python
komentar pada python, di tandai menggunakan `#` yang artinya kode tersebut tidak dieksekusi atau tidak dijalankan oleh mesin. Komentar hanya digunakan untuk menandai atau memberikan keterangan tertulis pada script.

Manfaat dari komentar tersebut, dapat memberikan keterangan mengenai script, code agar orang lain dapat memahami isi dari program anda.

Berikut contoh script yang menggunakan komentar pada python

```python
# ini komentar menggunakan tanda '#' yang tidak dapat dieksekusi
#Baris satu (1)
#Baris dua  (2)

'''
Ini adalah komentar yang berisikan penjelasan lebih
satu baru yaitu dengan menggunakan tanda petik satu ''
'''

"""
Ini contoh komentar menggunakan 
tanda kutip dua ""
"""

print("Hello World") #output text/string
#print('Hello World')

# Menggunakan Spesial karakter !@#$%^&*(),./;'[]\ pada komentar
```


## Penerapan konsep tipe data

### Tipe data
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
