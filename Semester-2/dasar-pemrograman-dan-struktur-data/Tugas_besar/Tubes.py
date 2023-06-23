# Membuat program konversi menggunakan fungsi

while(True):
    # Konversi data
    def data():
        print("\n1. MB to KB, \n" + "2. GB to KB, \n" + "3. TB to MB \n", end='', flush=True)
        angka = int(input('Masukan Pilihan: '))
        if(angka == 1):
            inputNilai1 = float(input('\nMasukan Megabyte: '))
            result = inputNilai1 * 1000
            print(str(result) + " Kilobyte")
        elif(angka == 2):
            inputNilai1 = float(input('\nMasukan Gigabyte: '))
            result = inputNilai1 * 10 ** 6
            print(str(result) + " Kilobyte")
        else:
            inputNilai1 = float(input('\nMasukan Terabyte: '))
            result = inputNilai1 * 1048576
            print(str(result) + " Megabyte")

    # Konversi kecepatan
    def kecepatan():
        print("\n1. Knot to KM/h,0 \n" + "2. KM/h to Knot, \n" + "3. M/h to KM/h \n", end='', flush=True)
        angka = int(input('Masukan Pilihan: '))
        if(angka == 1):
            inputNilai1 = float(input('\nMasukan Knot: '))
            result = inputNilai1 * 1.852
            print(str(result) + " KM/h")
        elif(angka == 2):
            inputNilai1 = float(input('\nMasukan KM/h: '))
            result = inputNilai1 / 1.852
            print(str(result) + " Knot")
        else:
            inputNilai1 = float(input('\nMasukan Mph: '))
            result = inputNilai1 * 1.609
            print(str(result) + " KM/h")

    # Konversi massa
    def massa():
        print("\n1. kg to gr, \n" + "2. gr to kg, \n" + "3. lb to kg, \n" + "4. kg to lb\n", end='', flush=True)
        angka = int(input('Masukan Pilihan: '))
        if(angka == 1):
            inputNilai1 = float(input('\nMasukan Kilogram: '))
            result = inputNilai1 * 1000
            print(str(result) + " gr")
        elif(angka == 2):
            inputNilai1 = float(input('\nMasukan Gram: '))
            result = inputNilai1 / 1000
            print(str(result) + " kg")
        elif(angka == 3):
            inputNilai1 = float(input('\nMasukan Pound/lb: '))
            result = inputNilai1 / 2.205
            print(str(result) + " kg")
        else:
            inputNilai1 = float(input('\nMasukan Kilogram: '))
            result = inputNilai1 * 2.205
            print(str(result) + " lb")

    # Konversi panjang
    def panjang():
        print("\n1. feet to meter, \n" + "2. meter to feet, \n" + "3. meter to km, \n" + "4. inchi to cm")
        angka = int(input('Masukan Pilihan: '))
        if(angka == 1):
            inputNilai1 = float(input('\nMasukan Feet: '))
            result = inputNilai1 / 3.281
            print(str(result) + " m")
        elif(angka == 2):
                inputNilai1 = float(input('\nMasukan Meter: '))
                result = inputNilai1 * 3.281
                print(str(result) + " ft")
        elif(angka == 3):
            inputNilai1 = float(input('\nMasukan Meter: '))
            result = inputNilai1 / 1000
            print(str(result) + " km")
        else:
            inputNilai1 = float(input('\nMasukan Inchi: '))
            result = inputNilai1 * 2.54
            print(str(result) + " cm")

    # Konversi suhu
    def suhu():
        print("\n1. celcius to farenheit, \n" + "2. celcius to kelvin, \n" + "3. farenheit to celcius, \n" + "4. farenheit to kelvin")
        angka = int(input('Masukan Pilihan: '))
        if(angka == 1):
            inputNilai1 = float(input('\nMasukan Celcius: '))
            result = inputNilai1 * 9 / 5 + 32
            print(str(result) + " F")
        elif(angka == 2):
            inputNilai1 = float(input('\nMasukan Celcius: '))
            result = inputNilai1 + 273.15
            print(str(result) + " K")
        elif(angka == 3):
            inputNilai1 = float(input('\nMasukan Farenheit: '))
            result = (inputNilai1 - 32) * 5 / 9
            print(str(result) + " C")
        else:
            inputNilai1 = float(input('\nMasukan Farenheit: '))
            result = (inputNilai1 - 32) * 5 / 9 + 273.15
            print(str(result) + " K")

    # Konversi waktu
    def waktu():
        print("\n1. jam to detik, \n" + "2. jam to milidetik, \n" + "3. hari ke menit, \n" + "4. minggu ke jam")
        angka = int(input('Masukan Pilihan: '))
        if(angka == 1):
            inputNilai1 = float(input('\nMasukan Jam: '))
            result = inputNilai1 * 3600
            print(str(result) + " detik")
        elif(angka == 2):
            inputNilai1 = float(input('\nMasukan Jam: '))
            result = inputNilai1 * 3.6 ** 6
            print(str(result) + " milidetik")
        elif(angka == 3):
            inputNilai1 = float(input('\nMasukan Hari: '))
            result = inputNilai1 * 1440
            print(str(result) + " menit")
        else:
            inputNilai1 = float(input('\nMasukan Minggu: '))
            result = inputNilai1 * 168
            print(str(result) + " jam")

    # Main/program utama
    print("SELAMAT DATANG DI ALGORITMA KONVERSI")
    print("Tersedia 6 pilihan konversi yaitu:\n")
    print('-------------------------------------------------------------')
    print("1. Konversi Data, \n" + "2. Konversi Kecepatan, \n" + "3. Konversi Massa, \n" + "4. Konversi Panjang, \n" + "5. Konversi Suhu, \n" + "6. Konversi Waktu")

    jeniskonversi = int(input('Masukan Pilihan: '))

    if(jeniskonversi == 1):
        data()
    elif(jeniskonversi == 2):
        kecepatan()
    elif(jeniskonversi == 3):
        massa()
    elif(jeniskonversi == 4):
        panjang()
    elif(jeniskonversi == 5):
        suhu()
    else:
        waktu()

    # looping program
    print('-------------------------------------------------------------')
    ulang = input('\nApakah ingin mengulang program? [Y or N]: ')
    if((ulang == 'N') or (ulang == 'n')):
        break
    else:
        match so:
            case 'nt': os.system('cls')
        for i in range(1, 30):
            print('-', end='')
