import os
so = os.name
match so:
    case 'nt': os.system('cls')


print('program 1')

list = [1, -2, -8, 0, 3]
if(len(list) == 0):
    print('list kosong')
else:
    max = max(list)
print('Nilai dari list: ', list)
print('Nilai max: ', max)
print('')

print('program 2')

list = [1, -2, -8, 0, 3]
if(len(list) == 0):
    print('list kosong')
else:
    min = min(list)
print('Nilai dari list: ', list)
print('Nilai min: ', min)
print('')

print('Program 3')
teks = 'pada hari minggu, cong dan cing belajar di rumah cung di Jl. Undata No 3 Kota Palu'

kata_list = teks.split()
kata_lebih_dari_4 = []
for kata in kata_list:
    if(len(kata) > 4):
        kata_lebih_dari_4.append(kata)
print(teks)
print(', ', kata_lebih_dari_4)

print('')
print('Program 4')

x = ['saya', 'makan', 'kuda']
x.reverse()
print(x)


