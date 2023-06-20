nama = input('Masukan nama: ')
nilai = int(input('Masukan nilai: '))

if(nilai >= 70):
    print(nama, 'lulus')
else:
    print(nama, 'tidak lulus')


tahun = int(input('masukan tahun: '))

if(tahun % 4 == 0):
    print('tahun kabisat')
else:
    print('bukan tahun kabisat')


angka = int(input('masukan angka: '))
gajil = 0
genap = 0
i = 0

while(i < angka):
    i += 1
    print(i, end=' ')
    if(i % 2 == 0):
        genap += 1
    else:
        gajil += 1
print('\nbilangan ganil', gajil)
print('bilangan genap', genap)


def kalkulator(angka1, angka2):
    print(angka1 + angka2)
    print(angka1 - angka2)
    print(angka1 * angka2)
    print(angka1 / angka2)

kalkulator(2, 3)

def string():
    kata = str(input('Masukan kata: '))
    upper = 0
    lower = 0


    for i in kata:
        if(i.islower()):
            lower += 1
        elif(i.isupper()):
            upper += 1
    print(upper)
    print(lower)

string()


list = [1, -2, -8, 0, 3]
print(max(list))

print(min(list))
