# Rekap Materi part 2

# upper () kapital
# lower() # normal
# isupper() # mengecek karakter kapital bernilai boolean
# islower() # mengecek karakter normal bernilai boolean
# istitle() # Mengecek karakter kapital dalam bentuk sebuah judul kek film
# startswith() # Mengecek karakter awal bernilai boolean 
# endswith() # Mengecek karakter akhir bernilai boolean 
# join() Membuat tambahan karakter spesial di dalam variabel 
# split() Menghilangkan karakter dan membuat list itu lagi
# rjust() rata kanan dengan karakter spesial
# ljust() rata kiri dengan karakter spesial
# center() rata tengah 
# strip() Menghilangkan karakter tergantung ("")


# upper ()
print("\nupper()")
nama1 = "Radit"
upper = nama1.upper() # hasil nya akan menjadi kapital
print(upper)

# lower()
print("\nlower()")
nama2 = "RADIT"
lower = nama2.lower()
print(lower)

# Mengecek karakter tersebut memiliki kapital atau normal 
# Menggunakan isupper
# menggunakan islower()

# isupper()
print("\nisupper()\n")
isupper = nama1.isupper()
print("---------------------------------------------")
print(nama1 + " isupper satu kapital = " + str(isupper)) # hasil nya false karena karakter memiliki huruf kecil 

print("---------------------------------------------")

# untuk mengecek karakter tersebut bernilai True
# harus memakai karakter kapital semua
nama1 = "RADIT"
isupper_kapital = nama1.isupper()
print(nama1 + " isupper full kapital = " + str(isupper_kapital)) # maka hasil nya akan true
print("---------------------------------------------")


print("\nislower()\n")
# islower()
nama1 = "radit"
islower_normal = nama1.islower()
print(nama1 + " islower huruf kecil semua = " + str(islower_normal))
print("---------------------------------------------")
# islower() salah satu kapital 
nama1 = "Radit"
islower_salahsatukapital = nama1.islower()
print(nama1 + " is lower kapital diawal = " + str(islower_salahsatukapital))
print("---------------------------------------------")

# awal kapital
print("\nistitle() judul yang harus diawali kapital\n")
nama1 = "Radit"
istitle = nama1.istitle()
print("---------------------------------------------")
print(nama1 + " istitle diawal kapital = " + str(istitle))
# hasil nya akan true karena di huruf Radit di awal memiliki huruf Kapital Radit


# awal huruf kecil 
nama1 = "rADIT"
istitle = nama1.istitle()
print(nama1 + " istitle diawal kecil = " + str(istitle))
# maka hasil nya akan false
print("---------------------------------------------")

# startswith() dan endswith()
# startswith()
print("\nstartswith()\n")
nama1 = "Muhammad"
print("Mengecek karakter M diawal")
startswith = nama1.startswith("M") # mengecek karakter awal adalah M kapital
print(nama1 + " startswith() M di awal? = " + str(startswith)) # maka hasil nya true karena awal adalah M


# endswith()
print("\nendswith()\n")
nama1 = "Muhammad"
print("Mengecek karakter M diakhir")
endswith = nama1.endswith("M") 
print(nama1 + " endswith() M di akhir? = " + str(endswith))
# hasil ini akan false karena huruf akhir bukan M tapi d
print("---------------------------------------------")

# atau bisa seperti ini 
# versi 2 startswith() 
# seperti ini maka hasil nya tetap akan true karena
# masih sesuai di variabel nama1 
print("\nstartswith() nama full di awal dan akhir\n")
nama1 = "Muhammad Raditya Ramadhan"
startswith = nama1.startswith("Muhammad Raditya")
print("teks awal menggunakan startswith()")
print(nama1 + " startswith Dari Muhammad Raditya = " + str(startswith))
nama1 = "Muhammad Raditya Ramadhan"
startswith = nama1.startswith("Ramadhan")
print(nama1 + " startswith Ramadhan = " + str(startswith))
print("---------------------------------------------")

# atau bisa seperti ini versi 2 endswith()
print("\nendswith() nama full di awal dan akhirl\n")
# awal
nama1 = "Muhammad Raditya Ramadhan"
endswith = nama1.endswith("Muhammad Raditya")
print("teks awal menggunakan endswith()")
print(nama1 + " endswith dari Muhammad Raditya = " + str(endswith))
# ini akan false dikarenakan endswith untuk mengecek teks terakhir
# maka 
nama1 = "Muhammad Raditya Ramadhan"
endswith = nama1.endswith("Ramadhan")
print(nama1 + " endswith Ramadhan = " + str(endswith))
print("---------------------------------------------")


# khusus join() kita akan memakai list
# join()
print("\njoin()\n")
nama = ['Muhammad','Raditya','Ramadhan']
print(nama)
print("\njoin() pisah Menghilangkan kurung dan menggunakan koma\n")
join_pisah = ','.join(nama) # Menghilangkan list hanya menamabahkan nama dan koma
print(join_pisah)
print("\njoin() pisah spasi\n")
join_pisah_spasi = ' '.join(nama)
print(join_pisah_spasi)
print("\njoin() Menggunakan huruf\n")
tambahan_dengan_karakter_abcd = ' ehm '.join(nama)
print(tambahan_dengan_karakter_abcd)
print("---------------------------------------------")


# split()
# Menghilangkan karakter dan membuat list 
print("\nsplit()\n")
# memanggil variabel sesuai output terminal yang ehm 
print("split() Menghilangkan karakter ehm")
nama = "Muhammad ehm Raditya ehm Ramadhan"
Menghilangkan_karakter = nama.split("ehm") # output terminal
print(Menghilangkan_karakter)
print("---------------------------------------------")

# rjust() , ljust() , center()
# rjust membuat teks rata kanan menggunakan karakter lain juga bisa
# dan bisa menamabahkan angka nya lebih dari 10 
print("\nrjust() rata kanan\n")
nama = 'Radit'
rjust = nama.rjust(10) # panjang 10
print("'"+rjust+"'")

print("\nljust() rata kiri\n")
nama = 'Radit'
ljust = nama.ljust(10) # panjang 10
print("'"+ljust+"'")

print("\ncenter() rata tengah\n")
nama = 'Radit'
center = nama.center(10) # panjang 10
print("'"+center+"'")
print("---------------------------------------------")

#strip ()
print("\nMenghilangkan suatu karakter\n")
nama = 'Radit'
strip = nama.strip("R")
print(strip)
print("---------------------------------------------")
