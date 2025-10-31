# String dan allignment 

# Width and multiline 

data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 150.1 
data_nomor_sepatu = 44 



# String standar  menggunakan format str
print("="*50)
print("\nData string\n")
data_string = f'nama = {data_nama}, umur = {data_umur}, data tinggi = {data_tinggi}, data nomor sepatu = {data_nomor_sepatu}'
print(data_string)


# String multiline menggunakan \n akan membuat line baru (new Newline) 
print("="*50)
print("\nData string Newline\n")
data_string = f'nama = {data_nama}, \numur = {data_umur}, \ndata tinggi = {data_tinggi}, \ndata nomor sepatu = {data_nomor_sepatu}'
print(data_string)
print("="*50)


# String multi line (kutip triples) f""" """
# didalam format str dia tetap akan bisa menampilkan variabel di sebelah nya 
# jika ada spasi di dalam f """ """ maka dia akan berubah menjadi spasi 
print('\nString menggunakan f""" (kutip triples)\n')
data_string = f"""nama = {data_nama} , umur = {data_umur}
umur = {data_umur}
tinggi = {data_tinggi}
"""
print(data_string)
print("="*50)


# Mengatur lebar
# menggunakan {data_nama:>5} maka akan bergeser 5 kali
# atau menggunakan angka lain 
# menggunakan :>angka 
data_nama = 'radit'
print('\nString menggunakan f""" (kutip triples)\n')
data_string = f"""
nama                   = {data_nama:>10} 
umur                   = {data_umur:>10}
tinggi                 = {data_tinggi:>10}
sepatu                 = {data_nomor_sepatu:>10}
"""
print(data_string)
#
#
