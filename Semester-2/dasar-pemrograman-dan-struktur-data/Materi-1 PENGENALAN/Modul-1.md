# 1. Syntax dasar pada Python

## Pendahuluan
Algoritma adalah urutan aksi-aksi yang dinyatakan dengan jelas dan tidak rancu untuk memecahkan suatu masalah dalam rentang waktu tertentu. Setiap aksi harus dapat dikerjakan dan mempunyai efek tertentu.

Algoritma dapat dituliskan dengan banyak cara, mulai dari menggunakan bahasa alami yang digunakan sehari-hari, simbol grafik bagan alir, sampai menggunakan bahasa pemograman seperti bahasa Python

## Syntax dasar
`print()` merupakan salah satu fungsi dari python untuk mencetak, dengan meletakkan kurung buka dan kurung tutup, untuk di Python versi 2.x tidak perlu menggunakan kurung buka dan tutup atau kurung kurawal `()`, cukup dipisahkan dengan spasi.

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

## Case Sensitivity
bahasa pemrograman python bersifat case sensitive, yang artinya huruf besar dan huruf kecil memiliki perbedaan. sebagai contoh seperti pada contoh program di atas,menggunakan `print()` akan langsung menampilkan output nya, selanjutnya jika menggunakan `Print()`, `PRINT()`, `PrInT()` atau fungsi tidak lengkap seperti `prnt()` akan muncul pesan error.

NOTE: perlu diperhatikan, case sensitive juga berlaku untuk function lainnya.

## Komentar pada Python
komentar pada python, di tandai menggunakan `#` yang artinya kode tersebut tidak dieksekusi atau tidak dijalankan oleh mesin. Komentar hanya digunakan untuk menandai atau memberikan keterangan tertulis pada script.

Manfaat dari komentar tersebut, dapat memberikan keterangan mengenai script, code agar orang lain dapat memahami isi dari program Anda.

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

