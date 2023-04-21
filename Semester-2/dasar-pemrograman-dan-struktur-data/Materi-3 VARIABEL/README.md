# Penerapan konsep variabel

## Variabel
Variabel adalah suatu pengenal (identifier) yang digunakan untuk mewakili suatu nilai tertentu di dalam proses program. Berbeda dengan konstanta yang nilainya selalu tetap, nilai dari suatu variable bisa diubah-ubah sesuai kebutuhan.

Variabel secara umumnya dapat menyimpan berbagai macam tipe data. di dalam Python, variabel bersifat dinamis, yang artinya python tidak perlu dideklarasikan tipe data tertentu dan variabel python dapat diuaah saat program dijalankan.

nama dari suatu variabel dapat ditentukan sendiri oleh pemrogram dengan aturan sebagai berikut:

- Terdiri dari gabungan huruf dan angka dengan karakter pertama harus berupa huruf. Bahasa python bersifat case-sensitive artinya huruf besar dan kecil dianggap berbeda. Jadi antara nama, Nama dan NaMa dianggap berbeda.
- Karakter pertama harus berupa huruf atau garis bawah atau underscore _ karakter selanjutnya dapat berupa huruf, garis bawah atau angka
dalam penulisan variabel pada python, cukup menuliskan variabel lalu mengisikannya dengan nilai ditambahkan dengan tanda sama dengan = diikuti dengan nilai untuk variabel tersebut.

Berikut penggunaan variabel dalam bahasa pemrograman python

```python

#memasukkan data dalam sebuah variabel
name = "Ledwin W" #isi variabel berupa string
print(name) #mencetak variabel

#nilai dan tipe data dalam variabel
age = 21 #tipe data angka / numeric
print(age) #mencetak nilai age
print(type(age)) #melihat tipe data dari age
age = "dua puluh satu" #tipe data string
print(age) #mencetak string dari age
print(type(age)) #melihat tipe data

first_name = "Ledwin"
middle_name = "Ezkiel"
last_name = "Wotulo"
name = first_name+" "+middle_name+" "+last_name
age = 19
hobby = "Belajar Coding"
print("Profil\n",name,"\n",age,"\n",hobby)

#contoh variabel lainnya
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_) #mencetak variabel

```

```
output

Ledwin W
21
<class 'int'>
dua puluh satu
<class 'str'>
Profil
Ledwin Ezkiel Wotulo 
19 
Belajar Coding
1 2 3 4 5 6 7 8
```
