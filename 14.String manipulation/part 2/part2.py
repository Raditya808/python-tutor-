# Part 2 

# Operator dalam bentuk methods 

## Merubah case dari string 

# merubah semua ke upper case


# variabel.upper() <- membuat teks menjadi kapital 
# variabel.lower() <- Membuat suatu teks menjadi huruf normal 
# variabel.islower() <- untuk pengecekan apakah lower case semua / huruf kecil
# variabel.isupper() <- untuk pengecekan apakah upper case semua / huruf kapital
# variabel.istitle() <- Judul yang harus diawali huruf kapital kek di film
# variabel.startswith() <- Pengecekan awal kata 
# variabel.endswith() <- pengecekan kata akhir
# variabel.join() penggabungan menggunakan '' dengan karakter apapun
# variabel.split() membuat suatu list
# variabel.rjust() dengan print("'"+"'") membuat rata kiri dengan string 
# variabel.ljust() dengan print("'"+"'") membuat rata kanan dengan string
# menghilangkan karakter menggunakan strip() dengan print("'"+kanan+"'")

# bagian bawah ini belum 
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)



print("-------------------------------")
print("\nVersi normal\n")
salam = "bro!"
print("Normal = " + salam)# versi normal 

print("\nVersi upppercase\n")
salam = salam.upper() # akan membuat teks nya dalam bentuk uppercase = kapital 
print("Upper = " + salam)
print("-------------------------------")

# merubah semua ke lower case
print("\nVersi normal\n")
alay = "aKu cInTa kAmU sEpErTiNya" # teks asli ada kapital 
print("Normal = " + alay)

print("\nVersi lowercase\n")
alay = "aKu cInTa kAmU sEpErTiNya" # teks nya menjadi normal 
alay = alay.lower() # akan membuat teks nya dalam bentuk lower = normal 
print("Lower = " + alay)
print("-------------------------------")
# jadi apa fungsi kedua kode ini ?
# lower = membuat teks kapital menjadi normal 
# upper = membuat teks menjadi kapital



## Pengecekan menggunakan isx method 
# contoh untuk pengecekan lowercase
 
print("\nPengecekan lowercase dalam bentuk boolean\n")
salam = "sist"
apakah_variabel_ini_lower = salam.islower() # hasil nya akan bool
print(salam + " is lower = " + str(apakah_variabel_ini_lower)) # jadi harus di konversi ke str terlebih dahulu

print("\nPengecekan upper dalam bentuk boolean\n")
salam = "sist"
apakah_variabel_ini_upper = salam.isupper() # hasil nya akan bool
print(salam + " is upper = " + str(apakah_variabel_ini_upper))
print("-------------------------------")
# jadi kedua kode ini akan mengecek 
# dari variabel salam 
# apakah kdedua kode itu ada kapital atau huruf kecil maka hasil nya akan boolean 


# pengecekan istitle
print("\nPengecekan title dalam bentuk boolean Menggunakan istitle()\n")
judul = "It Is Okay To Not To Be Orkay" # diawali dengan kapital maka hasil nya akan true dan tidak boleh ada char spesial
cek_judul = judul.istitle()
print(judul + " is title nya = " + str(cek_judul))
print("-------------------------------")

# mengecek komponen startswith() / endwith()
# awal kata / startswith()
print("\nPengecekan awal kata menggunakan startswith()\n")
cek_start = "Sangjanggin oppa".startswith("S") # hasil nya true karena awal kata ada S jika huruf lain maka akan false
print("Startswith = " + str(cek_start))


# kata akhir / endwith()
print("\nPengecekan kata akhir menggunakan endswith()\n")
cek_end = "Sangjanggin oppa".endswith("a") # hasil nya akan true karena akhir kata adalah a 
print("Endswith = " + str(cek_end))
print("-------------------------------")


# Penggabungan komponan join() / split()
print("\nPenggabungan menggunakan join()\n")
print("\nNormal list\n")
pisah = ['Muhammad','Raditya','Ramadhan']
print(pisah)
print("\nMenggunakann join() dengan string koma\n")
gabungan = ','.join(pisah) # menggunakan koma
print(gabungan)
# menggunakan spasi kosong / string kosong
print("\nMenggunakan single quote / string spasi kosong\n")
gabungan = ' '.join(pisah)
print(gabungan)
print("\nMenggunakan string ehm\n")
gabungan = ' ehm '.join(pisah)
print(gabungan)

# gabungan menggunakan split()
print("\nPenggabungan menggunakan split()\n")
gabungan = "Muhammad ehm Raditya ehm Ramadhan"
print(gabungan.split("ehm")) # maka ehm akan dihilangkan dan nama Muhamamd Raditya Ramadhan akan dijadikan list lagi
print("-------------------------------")



## alokasi karakter menggunaknan rjust() , ljust(), center()

# rjust
print("\nAlokasi karakter menggunakan rjust() rata kanan\n")
kanan = "kanan".rjust(10) # batas ke kanan = 10
print("'"+kanan+"'")

# ljust
print("\nAlokasi karakter menggunakan ljust() rata kiri\n")
kiri = "kiri".ljust(10) # batas ke kiri = 10
print("'"+kiri+"'")

# center
print("\nAlokasi karakter menggunakan center() rata tengah\n")
tengah = "tengah".center(10) # batas tengah 10
print("'"+tengah+"'")
print("-------------------------------")



# Menggunakan rjust() dengan karakter spesial
print("\nKarakter spesial menggunakan rjust()")
kanan = "kanan".rjust(20,"+")
print("'"+kanan+"'")


# Menggunakan ljust() dengan karakter spesial
print("\nMenggunakan karakter spesial ljust()")
kiri = "kiri".ljust(20,"+")
print("'"+kiri+"'")


# Menggunakan karakter spesial center() 
print("\nKarakter spesial menggunakan center()")
tengah = "tengah".center(20,"+")
print("'"+tengah+"'")
print("-------------------------------")


# Kebalikan -> strip()
tengah = "tengah".strip("+") # maka akan menghilangkan karakter +
print("'"+tengah+"'")

# kanan 
kanan = "kanan".strip()
print("'"+kanan+"'")
