# Set saldo awal
saldo = 10000000

# Set PIN
PIN = "1234"

# Fungsi untuk meminta input PIN
def masukkan_PIN():
    pin = input("Masukkan PIN: ")
    return pin

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("=== Mesin ATM ===")
    print("1. Cek saldo")
    print("2. Tarik tunai")
    print("3. Simpan uang")
    print("4. Keluar")

# Fungsi untuk menampilkan saldo
def tampilkan_saldo():
    print("Saldo anda saat ini adalah Rp", saldo)

# Fungsi untuk melakukan penarikan tunai
def tarik_tunai():
    global saldo
    jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: "))
    if jumlah > saldo:
        print("Saldo tidak mencukupi")
    else:
        saldo -= jumlah
        print("Penarikan berhasil. Saldo anda saat ini adalah Rp", saldo)

# Fungsi untuk menambahkan uang ke dalam akun
def simpan_uang():
    global saldo
    jumlah = int(input("Masukkan jumlah uang yang ingin disimpan: "))
    saldo += jumlah
    print("Simpan uang berhasil. Saldo anda saat ini adalah Rp", saldo)

# Program utama
while True:
    pin = masukkan_PIN()
    if pin == PIN:
        print("PIN benar. Selamat datang di mesin ATM.")
        break
    else:
        print("PIN salah. Silakan coba lagi.")

while True:
    tampilkan_menu()
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        tampilkan_saldo()
    elif pilihan == 2:
        tarik_tunai()
    elif pilihan == 3:
        simpan_uang()
    elif pilihan == 4:
        print("Terima kasih telah menggunakan mesin ATM.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
