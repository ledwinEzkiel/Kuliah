# program 1

tuple = ('K', 'O', 'M', 'P', 'U', 'T', 'E', 'R')

konversi_dict = {
    'K':'Komputer', 
    'O':'', 
    'M':'', 
    'P':'', 
    'U':'', 
    'T':'', 
    'E':'', 
    'R':'', 
}

hasil_konversi = ''
for karakter in tuple:
    if(karakter in konversi_dict):
        hasil_konversi += konversi_dict[karakter]
    else:
        hasil_konversi += karakter
print(hasil_konversi)


# program 2

data_dict = {
    'bil1': 90,
    'bil2': -54,
    'bil3': 0.4,
}

hasil_jumlah = sum(data_dict.values())
print(hasil_jumlah)

# program 3

hari_tuple = (
    'Senin',
    'Selasa',
    'Rabu',
    'Kamis',
    'Jumat',
    'Sabtu',
    'Minggu'
)

jumlah_hari = len(hari_tuple)
print("Jumlah hari dalam seminggu: ", jumlah_hari)