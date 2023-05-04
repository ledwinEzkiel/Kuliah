import os
so = os.name
match so:
    case 'nt': os.system('cls')

# progam 1
a = "Hello World"

print("Karakter pada index ke-2:", a[2])
print("Karakter pada index ke-4:", a[4])
print("Karakter pada index ke-8:", a[4])
print("Karakter pada index ke-10:", a[9])

# program 2
a = "Hello World"

# Menampilkan karakter pada index ke 1 sampai 3
print(a[1:3])  # Output: el

# Menampilkan karakter pada index ke 2 sampai 5
print(a[2:6])  # Output: llo

# Menampilkan karakter pada index ke 7 sampai 11
print(a[6:10])  # Output: worl


# program 3

original_string = 'Hello , World'
print(original_string.lower())
print(original_string.upper())
kata = 'orang jahat adalah orang baik yang tersakiti'
x = kata.replace('a', 'i').replace('o', 'i').replace('e', 'i')
print(x)