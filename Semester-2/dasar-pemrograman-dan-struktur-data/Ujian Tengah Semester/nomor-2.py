# Buat program dengan menampilkan sebuah perulangan piramida dengan menampilkan karakter emoji smile \U0001f600

rows = 6

for i in range(rows):
    for j in range(i+1):
        print("\U0001f600", end="")
    print("")
