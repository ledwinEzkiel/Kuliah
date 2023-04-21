import os 
so = os.name
match so:
    case 'nt': os.system('cls')

# biodata
deskripsi = "Ini program python"
nama = "Ledwin"
alamat = "Palu"
umur = 18
hobi = "Belajar Coding"

print("Nama saya", nama, "yang beralamat di ", alamat, ", umur sekarang", umur, "tahun dan memiliki hobi", hobi, "\n")

# mengitung luas dan keliling persegi panjang
panjang = 15
lebar = 5.7

keliling_persegi_panjang = panjang * lebar
lebar_persegi_panjang = 2*(panjang + lebar)
print(f"sebuah persegi panjang dengan lebar sebesar {lebar_persegi_panjang} dan keliling {keliling_persegi_panjang}\n")

# mengitung luas dan keliling lingakaran

jari_jari  = 15
phi = 3.14
keliling_lingkaran = 2 * phi * jari_jari
luas_lingkaran = phi * jari_jari * jari_jari

print(f"sebuah lingkaran dengan jari-jari {jari_jari} cm memiliki luas sebesar {luas_lingkaran} dan keliling {keliling_lingkaran}")