# Buat program dengan menampilkan nilai median dari tiga bilangan, dengan penjelasan sebagai berikut, misalkan ada 3 bilangan, secara acak 23, 65, 12 maka jika di urutkan dari nilai terendah ke terbesar menjadi 12, 23, 65 dan nilai mediannya adalah 23
# Input tiga bilangan

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Menentukan nilai median
nilai = [a, b, c]
nilai.sort()
median = nilai[1]

# Menampilkan output
print("Bilangan yang dimasukkan:", nilai)
print("Nilai median:", median)