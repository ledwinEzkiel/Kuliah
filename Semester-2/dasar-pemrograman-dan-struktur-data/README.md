
# Dasar Pemrograman & Struktur Data

Semua file ini merupakan bahasa pemrograman Python

### Nested Loop

Bahasa pemrograman Python memungkinkan penggunaan satu lingkaran di dalam loop lain. Bagian berikut menunjukkan beberapa contoh untuk menggambarkan konsep tersebut.

Dibawah ini adalah contoh penggunaan Nested Loop.

```python
#Contoh penggunaan Nested Loop
#Catatan: Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai True(benar) dan nol sebagai False(salah)

i = 2
while(i < 100):
  j = 2
while(j <= (i/j)):
  if not(i%j): break
  j = j + 1
  if (j > i/j) : print(i, " is prime")
    i = i + 1

print("Good bye!")
```

testing
