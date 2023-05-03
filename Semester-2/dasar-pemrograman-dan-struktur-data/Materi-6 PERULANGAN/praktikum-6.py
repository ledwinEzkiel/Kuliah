# program 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
genap = 0
ganjil = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    i += 1

print("List angka:", numbers)
print("Jumlah bilangan genap:", genap)
print("Jumlah bilangan ganjil:", ganjil)


# program 2
number = int(input("Masukan angka: "))
for i in range(1, 11):
    print(number, "*", i, "=", number*i)

# program 3

n = 11
a, b = 0, 1

for i in range(n):
    print(b, end=" ")
    a, b = b, a + b