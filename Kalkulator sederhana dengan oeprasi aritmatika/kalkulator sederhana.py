# kalkulator sederhana

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print("Pilih operasi:")

if a == 0 and b == 0:
    print("Tidak ada operasi yang dipilih.")
else:
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Pangkat")
    print("6. Modulus")
    print("7. Floor Division")

    pilihan = int(input("Masukkan pilihan (1-7): "))

    if pilihan == 1:
        hasil = a + b
        print("hasil dari", a, "+", b, "adalah", hasil)
    if pilihan == 2:
        hasil = a - b
        print("hasil dari", a, "-", b, "adalah", hasil)
    if pilihan == 3:
        hasil = a * b
        print("hasil dari", a, "*", b, "adalah", hasil)
    if pilihan == 4:
        hasil = a / b
        print("hasil dari", a, "/", b, "adalah", hasil)
    if pilihan == 5:
        hasil = a ** b
        print("hasil dari", a, "**", b, "adalah", hasil)
    if pilihan == 6:
        hasil = a % b
        print("hasil dari", a, "%", b, "adalah", hasil)
    if pilihan == 7:
        hasil = a // b
        print("hasil dari", a, "//", b, "adalah", hasil)


