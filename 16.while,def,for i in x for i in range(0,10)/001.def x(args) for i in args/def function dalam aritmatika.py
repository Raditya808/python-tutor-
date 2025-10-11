# function dasar dalam artimatika
# contoh kode dibawah ini perhitungan dasar dalam function 
# versi pisah 

print("FUNCTION OUTPUT PISAH")
def hitung(a,b):
    a = a + b # operator tambah  
    b = a - b # dan kurang 
    return a, b 
a =int(input("Masukan angka : "))
b =int(input("Masukan angka : "))

tambah,kurang = hitung(a,b)

print(tambah)
print(kurang)

print("="*50)

print("FUNCTION OUTPUT GABUNG")
def hitung(a,b):
    a = a + b 
    b = a - b 
    return a,b 
a =int(input("Masukan angka : "))
b =int(input("Masukan angka : "))

tambah,kurang = hitung(a,b)
print(tambah,kurang)
# maka output nya akan tergabung