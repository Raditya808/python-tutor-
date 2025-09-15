nama_awal = "Muhammad"
nama_tengah = "Raditya"
nama_akhir = "Ramadhan"


print("\nDATA MANIPULASI PYTHON\n")
# contoh print tampah string kosong
print("=============================================")
nama_lengkap = nama_awal + nama_tengah + nama_akhir
print("Print gabungan")
print(nama_lengkap)
print("=============================================")
# output akan menggabungkan variabel nama_lengkap tanpa string kosong


'''
1. Mengprint menggunakan string kosong
'''

nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print("Menggunakan string kosong")
print(nama_lengkap)
print("=============================================")

# menentukan ukuran string menggunakan len(nama_lengkap) dan di konversi menggunakan str(penggabungan_len)
# Menghitung string spasi juga termasuk 
print("Menghitung string dalam variabel gabungan menggunakan variabel baru menggunakan len() dan dikonversi menggunakan str()")
print(nama_lengkap)
penggabungan_len = len(nama_lengkap)
print("Jumlah variabel nama_lengkap = " +  str(penggabungan_len))
print("=============================================")

# indexing 
print("Indexing menggunakan [0] dan [-0]")  # output nya akan mengeluarkan huruf awal di Muhammad yaitu 
print("Menggunakan [0]")
print("index ke -> 0  = " + nama_lengkap[0]) # M
print("index ke -> 1  = " + nama_lengkap[1]) # u
print("index ke -> 2  = " + nama_lengkap[2]) # h
print("index ke -> 3  = " + nama_lengkap[3]) # a
print("index ke -> 4  = " + nama_lengkap[4]) # m
print("index ke -> 5  = " + nama_lengkap[5]) # m                                          
print("index ke -> 6  = " + nama_lengkap[6]) # a                                      
print("index ke -> 7  = " + nama_lengkap[7]) # d
print("index ke -> 8  = " + nama_lengkap[8]) #  spasi dianggap kosong tetapi memiliki isi 
print("index ke -> 9  = " + nama_lengkap[9]) # R
print("index ke -> 10 = " + nama_lengkap[10]) # a
print("index ke -> 11 = " + nama_lengkap[11]) # d
print("index ke -> 12 = " + nama_lengkap[12]) # i
print("index ke -> 13 = " + nama_lengkap[13]) # t
print("index ke -> 14 = " + nama_lengkap[14]) # y
print("index ke -> 15 = " + nama_lengkap[15]) # a
print("index ke -> 16 = " + nama_lengkap[16]) #
print("index ke -> 17 = " + nama_lengkap[17]) # R
print("index ke -> 18 = " + nama_lengkap[18]) # a
print("index ke -> 19 = " + nama_lengkap[19]) # m
print("index ke -> 20 = " + nama_lengkap[20]) # a
print("index ke -> 21 = " + nama_lengkap[21]) # d
print("index ke -> 22 = " + nama_lengkap[22]) # h
print("index ke -> 23 = " + nama_lengkap[23]) # a
print("index ke -> 24 = " + nama_lengkap[24]) # n
print("=============================================")

print("\npenambahan print index berlebih akan menghasilkan eror\n")

print("Menggunakan [-0]")

print("index ke -> -0  = " + nama_lengkap[-0]) # 
print("index ke -> -1  = " + nama_lengkap[-1]) # 
print("index ke -> -2  = " + nama_lengkap[-2]) # 
print("index ke -> -3  = " + nama_lengkap[-3]) # 
print("index ke -> -4  = " + nama_lengkap[-4]) # 
print("index ke -> -5  = " + nama_lengkap[-5]) #                                          
print("index ke -> -6  = " + nama_lengkap[-6]) #                                      
print("index ke -> -7  = " + nama_lengkap[-7]) # 
print("index ke -> -8  = " + nama_lengkap[-8]) #   
print("index ke -> -9  = " + nama_lengkap[-9]) # 
print("index ke -> -10 = " + nama_lengkap[-10]) # 
print("index ke -> -11 = " + nama_lengkap[-11]) # 
print("index ke -> -12 = " + nama_lengkap[-12]) # 
print("index ke -> -13 = " + nama_lengkap[-13]) # 
print("index ke -> -14 = " + nama_lengkap[-14]) # 
print("index ke -> -15 = " + nama_lengkap[-15]) # 
print("index ke -> -16 = " + nama_lengkap[-16]) #
print("index ke -> -17 = " + nama_lengkap[-17]) # 
print("index ke -> -18 = " + nama_lengkap[-18]) # 
print("index ke -> -19 = " + nama_lengkap[-19]) # 
print("index ke -> -20 = " + nama_lengkap[-20]) # 
print("index ke -> -21 = " + nama_lengkap[-21]) # 
print("index ke -> -22 = " + nama_lengkap[-22]) # 
print("index ke -> -23 = " + nama_lengkap[-23]) # 
print("index ke -> -24 = " + nama_lengkap[-24]) # 
print("=============================================")

# Mengecek salah satu char di dalam variabel gabungan dengan in / not in
# dengan true false
print("\nprint variabel dan mengecek isi dari dari char tersebut apakah ada di dalam variabel nama_lengkap\n")
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
status = a in nama_lengkap
print(status)
status = b in nama_lengkap
print(status)
status = c in nama_lengkap
print(status)
status = d in nama_lengkap
print(status)
status = e in nama_lengkap
print(status)
status = f in nama_lengkap
print(status)
print("=============================================")

# min and max
print("\nmin and max\n")
print(nama_lengkap)
print("Paling kecil = " + min(nama_lengkap))
print("Paling besar = " + max(nama_lengkap)) # akan mengeluarkan output y karema dalam abc y paling akhir
print("=============================================")

# Pengulangan string Menggunakan aritmatika ("test"*20)
print("\nString pengulangan menggunakan kali *\n")
print("wk"*20)
# atau bisa dibalik output nya tetap sama
print(20*"wk")
print("=============================================")

# ascii menggunakan ord di ("")
# dan menggunakan str dan ach di (_variabel)
print("ascii_code")
ascii_code = ord(" ")
print("ascci adalah = " + str(ascii_code))
print(str(ascii_code))

data = 117 
print("data 117 = " + chr(data))
print(chr(data))
print("=============================================")

print("Menghitung seberapa banyak variiabel menggunakan count(_variiabel) dan str(_variiabel baru)")
random = "botong lontong acong kingkong hentong"
print("Macam macam o didalam = " + random)
jumlah = random.count("o")
print("=",jumlah)
print("jadi nilai o didalam " + random + " = " + str(jumlah)) # menggunakan str kalau tidak ada maka akan err
print("=============================================")