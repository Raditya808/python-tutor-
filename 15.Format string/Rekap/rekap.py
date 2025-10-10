# Rekap Materi Format string 

# f'' dalam tambahan variabel nama 

nama = "Radit"

format_string = f'halo {nama}'
print(format_string)

# dalam angka menggunakan f''

angka = 2005.5 
format_string = f'angka = {angka}'
print(format_string)

# menggunakan boolean dalam true atau false 
# True 
boolean = True 
format_string = f'boolean = {boolean}'
print(format_string)

# False
boolean = False 
format_string = f'boolean = {boolean}'
print(format_string)

# angka bilangan bulat
bilangan_bulat = 15 
format_string = f'bilangan bulat = {bilangan_bulat}'
print(format_string)

# bilangan ribuan / jutaan menggunakan {variabel:,} 
# ribuan 
angka = 2000
format_string = f'angka = {angka:,}'
print(format_string)

# atau jika jutaan juga menggunakan {variabel:,}
angka = 2000000
format_string = f'angka = {angka:,}'
print(format_string)


# bilangan desimal
# angka desimal menggunakan f'{angka:.3f/ :.2f}' f artinya bertipe float 
# karena di variabel ini memiliki tipe float karena ada koma 
angka_desimal = 2005.54321
format_string = f'angka desimal = {angka_desimal:.3f}' # akan menampilkan angka 2005.543 #

# 3f akan memunculkan angka setelah koma 
print(format_string)

# menggunakan {angka:.2f}
# 2f akan membuat 2 angka setelah koma mumcul
angka_desimal = 2005.54321
format_string = f'angka_desimal = {angka_desimal:.2f}' # menampilkan 2005.54
print(format_string)


# leading zero 
# menggunakan {angka:010.3f} atau {angka:9.3f}
# :010.3f penambahan 0 dua kali 010 memberikan spasi sebanyak 10 kali
angka = 2005.54321 
format_string = f'desimal = {angka:010.3f}'
print(format_string)

# :9.3f menghilangkan 2 nol kalau angka nya 9 dia memberikan spasi 9 kali dari niali variabel
angka = 2005.54321
format_string = f'desimal = {angka:9.3f}'
print(format_string)

# menampilkan plus minus atau karakter lain f'{variabel+d}' 
angka = +10
angka2 = -10 
format_string1 = f'angka = {angka:+d}'
format_string2 = f'angka = {angka2:+d}'
print(format_string1)
print(format_string2)


# Format string dalam aritmatika 
# Menggunakan f'{variabel * variabel}'
angka = 2000
jumlah = 10 

format_string = f'Harga total = {angka * jumlah}'
print(format_string)


# format persen menggunakan 
# f'{variabel:%}'
# atau bisa juga menggunakan 
# f'{variabel:.2%}' jika penambahan angka didepan nya untuk menghilangkan angka 0 dibelakang  
a = 0.0034 
format_persen = f'persen = {a:%}'
print(format_persen)

a = 0.0034
format_persen = f'persen = {a:.2%}'
print(format_persen)

# binary hex oct 
# dengan menggunankan f'{bin(angka)}'
angka = 115 
format_bin = f'format binary = {bin(angka)}'
format_oct = f'format oct = {oct(angka)}'
format_hex = f'format hex = {hex(angka)}'
print(format_bin)
print(format_oct)
print(format_hex)
