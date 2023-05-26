# program 1
print("prgram 1\n")
numbers = int(input("data n: "))
genap = 0
ganjil = 0
i = 0

while (i < numbers):
    i += 1
    print(i, end=" ")
    if i % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print("\nJumlah bilangan genap:", genap)
print("Jumlah bilangan ganjil:", ganjil)


# program 2
print("\nprgram 2\n")
number = int(input("\nMasukan angka: "))
for i in range(1, 11):
    print(number, "*", i, "=", number*i, )

# program 3
print("\nprgram 3\n")
n = 11
a, b = 0, 1

for i in range(n):
    print(b, end=" ")
    a, b = b, a + b
print("\n")
