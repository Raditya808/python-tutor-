import datetime as dt 

tahun = int(input('Masukan tahun: '))
bulan = int(input('Masukan bulan: '))
tanggal = int(input('Masukan tanggal: '))

full_data_lahir = dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir anda {full_data_lahir}')
print(f'hari = {full_data_lahir:%A}')
print("="*50)



output_tanggalhariini = dt.date.today()
print(f'hari ini adalah tanggal {output_tanggalhariini}')

uumur_hari = output_tanggalhariini - full_data_lahir
print(f'umur hari {uumur_hari}')

umuranda = uumur_hari.days // 365 
sisa_bulan = (uumur_hari.days % 365) // 30 
print(f'umur anda = {umuranda} Tahun {sisa_bulan} Bulan')




# DALAM PYTHON URUTAN UNTUK INPUT TANGGAL LAHIR SUDAH ADA DI CEK SYNTAX 
# dt.date.today() 
# 2005,10,17 DIMULAI TAHUN BULAN DAN TANGGAL



# rekap part 2 
import datetime as a 

# Mmebuat data tanggal lahir mengirim data parameter a 
# tanggal_lahir = a.date(2005,10,17)
# print(tanggal_lahir)

# Mengecek hari dalam bahasa inggris 
#tanggal_hari_ini = a.date.today()
#print(tanggal_hari_ini)

# Mengecek hari didalam bahasa inggris 
#hari_ini = a.date.today()
#print(f'Today is {hari_ini:%A}')

# Membuat input 
Tahun = int(input("Masukan Tahun: "))
Bulan = int(input("Masukan Bulan: "))
Tanggal = int(input("Masukan Tanggal: "))

# data hari ini beserta tanggal 
print("="*30)
hari_ini_tanggal = a.date.today()
print('Sekarang tanggal',hari_ini_tanggal)
print("="*30)

full_ktp = a.date(Tahun,Bulan,Tanggal)
print('Tanggal lahir anda =',full_ktp)

# Mengecek hari tanggal lahir sampe tahun sekarang
hari_nya = hari_ini_tanggal - full_ktp
print('Hari dari hari ini ke hari di tanggal lahir = ',hari_nya)

# Mengecek umur 
umur = (hari_nya.days // 365) # days disini berfungsi untuk mendapatkan output dalam bentuk integer 
sisa_bulan = (hari_nya.days % 365) // 30  # selalu ingat days untuk konfersi hari dan angka menjadi angka saja
print('anda berumur',umur,'Tahun dan',sisa_bulan,'Bulan')



