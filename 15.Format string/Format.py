# format streing menggunakan python
# materi 
# ========================================================================================================================================================================================================================
# f 'hello {nama}' tanpa harus konversi ke str 
# f'angka {angka}' tanpa harus konversi ke str 
# f'boolean {boolean}' tanpa harus konversi ke str
# versi true / versi false 
# menampilkan bilangan bulat f'{bilangan}' bilangan biasa 
# menambahkan {angka:,} di nilai variabel maka akan menambahkan koma
# {angka:.2f} maka akan menampilkan 2 angka dibelakang koma didalam nilai variabel 2005.54321 

# {angka:3.f} untuk spasi kosong dibelakang koma

# leading zero menggunakan f'{angka:010.3f}' maka akan menambahkan 0 di depan angka atau menggunakan f'{angka:9.3f}' maka menampilkan satu 0 dengan variabel 2005.54321 

# penambahan min dan plus atau + dan - menggunakan {angka:+d} maka akan menampilkan + dan - atau bisa menggunakan {:d.2f} maka akan menampilkan + dan - pada angka float
# menggunakan angka 0.45 format persen menggunakan {persen:%} maka akan menampilkan persen atau menggunakan {persen:.2%} maka akan menampilkan 2 angka dibelakang koma dan persen
# aritamtika {variabel * variabel}
# menggunakan angka 225 konvers {oct}, {hex}, {binary} 
# ========================================================================================================================================================================================================================




# contoh generic 
# string menggunakan f ''
print("="*50)
print("\nFORMAT STRING MENGGUNAKAN f''{}\n")
nama = "Radit"
format_str = f"hello {nama}"

print(format_str)

print("="*50)


# Angka Menggunakan f''
print("\nFORMAT ANGKA MENGGUNAKAN f''{}\n")
angka = 2005.5 
format_str = f'angka = {angka}' 
print(format_str)

print("="*50)


# bolean menggunakan f''
# Versi True
print("\nFORMAT BOOLEAN MENGGUNAKAN f''{}\n")
boolean = True 
format_str = f'boolean = {boolean}'
print(format_str)

# Versi false
boolean = False 
format_str = f'boolean = {boolean}'
print(format_str)
print("="*50)


# Bilangan bulat

# menggunakan f'{angka:d}' hanya berlaku untuk int sebenar nya 
# menggunakan f'{angka}' aja bisa tetapi ini hanya berlaku untuk 
# integer saja jika variabel nya nilai lain maka akan eror
print("\nANGKA BILANGAN BULAT MENGGUNAKAN f''{}\n")
angka = 15 
format_str = f'angka bilangan bulat = {angka:d}'
print(format_str)

# Bilangan dengan ordo ribuan

# fungsi {angka:,}
# akan membuat angka memiliki koma sesuai angka
print("\nBILANGAN RIBUAN MENGGUNAKAN f''{angka:,}\n")
angka = 2000000 # Output = 2,000,000 atau lebih 
format_str = f'ribuan = {angka:,}'
print(format_str)


# Bilangan desimal

print("\nANGKA DESIMAL MENGGUNAKAN f''{angka:.3f/2f}\n")
angka = 2005.54321 
format_str = f'angka desimal = {angka:.3f}' # akan menampilkan spasi kosong    
print(format_str)

print("="*50)
# fungsi .2f akan mengambil 2 angka dibelakang koma 
# dan ini berlaku hanya untuk tipe data float (berkoma di belakang angka)
# atau kalau mau mengambil 3 angka menggunakan .3f



# menampilkan leading zero
# f'{angka:010.3f}'  maka output nya 00 dua dari 10 baris angka
# f'{angka:9.3f}' maka ouput nya 0 satu dari 9 angka
# angka nya bebas
print("\nLEADING ZERO MENGGUNAKAN f''{angka:010.3f}\nATAU MENGGUNAKAN f''{angka:9.3f}\n")
angka = 2005.54321 
format_str1 = f'desimal = {angka:010.3f}'
format_str2 = f'desimal = {angka:9.3f}'

print(f"Menggunakan f''{'angka:10.3f'} akan menambahkan dua angka 0")
print(format_str1)

print(f"Menggunakan f''{'angka:9.3f'} akan membuat spasi")
print(format_str2)
print("="*50)


# Menampilkan angka tanda + atau - 
# Menggunakan f'{angka_minus:+d}' 
# maka kedua angka tersebut akan mengeluarkan plus minus nya + dan - 
print("\nMenampilkan plus minus menggunakan f'{:+d / +.2f}\n")
angka_minus = -10 
angka_plus = +10
angka_float = +10.1234
format_minus = f'minus = {angka_minus:+d}'
format_plus = f'plus = {angka_plus:+d}'
format_float = f'float = {angka_float:+.2f}'
print(format_minus)
print(format_plus)
print("atau menggunakan 2f jika angka nya float")
print(format_float)
print("="*50)


# memformat persen 
print("\nMEMFORMAT PERSEN MENGGUNAKAN f''{persen:% / :.2%}\n")
persentase = 0.045 
format_persen = f'persen = {persentase:%}'
print(format_persen)


# menggunakan :.2% 
persentase = 0.045 
format_persen = f'persen = {persentase:.2%}'
print(format_persen)
print("="*50)




# melakukan operasi artimatika di f'{harga * jumlah,}' dan menggunakan ,
print("\nMELAKUKAN OPERASI ARTIMATIKA DI f''{harga * jumlah:,}\n")
harga = 10000 
jumlah = 5 

format_string = f'harga total = RP {harga * jumlah}'
print(format_string)
print("="*20)


# format angka lain ('binary, octal ,hexadecimal')
angka = 225
format_binary = f'bin = {bin(angka)}'
format_octal = f'oct = {oct(angka)}'
format_hexadesimal = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hexadesimal)

