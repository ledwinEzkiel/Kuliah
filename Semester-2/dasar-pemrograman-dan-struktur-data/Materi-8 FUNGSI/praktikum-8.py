
# mnentukan faktorial

def faktorial():

    print('1. Program Python Menghitung Faktorial  ##')
    print()

    angka = int(input('Input angka: '))

    hasil = 1
    for i in range(1,angka+1):
        hasil = hasil * i

    print(angka,'! = ', hasil,sep='')

print(faktorial())


# menghitung uppercase dan lowercaase
print('\n2. program menghitung upercase dan lowercase\n')
def hitung_karakter(string):
    uppercase = 0
    lowercase = 0
    for char in string:
        if(char.isupper()):
            uppercase += 1
        elif(char.islower()):
            lowercase += 1
    return lowercase, uppercase
    
kata = input("Masukkan sebuah string: ")
uppercase, lowercase = hitung_karakter(kata)
print("Jumlah karakter uppercase pada string:", uppercase)
print("Jumlah karakter lowercase pada string:", lowercase)

# program 3
print('\n3. program memeriksa bilangan prima\n')
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Contoh pemanggilan fungsi
num = int(input("Masukkan bilangan: "))
if is_prime(num):
    print(num, "adalah bilangan prima")
else:
    print(num, "bukan bilangan prima")
