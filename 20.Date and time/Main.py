# Date and Time

# Menggunakan import datetime 

import datetime as dt  # mengimport datetime sebagai parameter dt  

# hari_ini = dt.date.today() # dt di inisialisasi ke syntax date today yang berarti untuk mengecek tanggal berapa sekarang 

# print(hari_ini) # output maka akan mengluarkan tanggal sesuai hari ini



# Membuat variabel baru dengan syntax date 
# Sesuai tanggal yang kita buat 
# tanggal = dt.date(2005,10,10)
# print(tanggal)



# Menginput data tanggal lahir beserta hari nya 
################################################################
print("Masukan tanggal sesuai \nbulan dan tahun lahir anda\n")
tanggal = int(input('Tanggal \t:')) # \t berfungsi membuat tab 
bulan   = int(input('Bulan \t\t:'))
tahun   = int(input('Tahun \t\t:'))

tanggal_lahir = dt.date(tahun,bulan,tanggal) # argumen ini harus sesuai dengan python dimana urutan untuk date adalah tahun,bulan,tanggal 
print(f'tanggal lahir anda secara lengkap = {tanggal_lahir}') 
################################################################

print("="*50)

# Mengecek hari ini dalam bahasa inggris dalam python
# dan mengecek umur 
# mengecek hari saat hari ini dan tanggal_lahir dikurang 
# membuat umur tahun menggunakan floor division 365 hari untuk mengecek umur tahun 
# membuat sisa umur bulan menggunakan modulus
# menggunakan days untuk mendapatkan output dalam bentuk integer
################################################################
hari_ini = dt.date.today() # mengecek tanggal hari ini 
print(f'Sekarang adalah tanggal = {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 # menggunakan floor division dan days
umur_bulan_sisa = (umur_hari.days % 365) // 30 # menggunakan days untuk mendapatkan output dalam bentuk integer  

print(f'Hari nya adalah = {tanggal_lahir:%A}') # Fungsi :%A itu untuk mengecek hari dalam bahasa inggris
print(f'umur anda adalah = {umur_tahun} Tahun, {umur_bulan_sisa} bulan')
################################################################
