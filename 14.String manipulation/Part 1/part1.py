#part 1 STRING MANIPULATION

#OPERASI DAN MANIPULASI STRING

# materi 
#====================================================================================================================
# penggabungan + penggabungan + 
# + " " + string kosong
# indexing [0] dan kebalikan [-0]
# Menghitung panjang string menggunakan len(nama_lengkap)
# Mengecek karakter menggunakan in dan not in
# mengulang string menggunakan print("wk"*20)
# ASCII code menggunakan str() chr() tergantung tipe data
# menentukan item min(nama_lengkap) dan max(nama_lengkap) menentukan abc tertinggi dalam variabel min = terkecil max = terbesar
# Operator method menggunakan count("contoh abc")
#====================================================================================================================



# (1. Menyambung string (concatenate))
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

# versi tergabung variabel dan tidak memberikan spasi
print('\n===================================================\n')

print("Output Menggunaka str kosong dan menggunakan single quote dan double quote ")
# MENGGABUNGKAN DENGAN STR KOSONG +" "+
# DAN MENGGUNAKAN SINGLE / DOUBLE QUOTE
nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

print('\n===================================================\n')

# untuk memberikan spasi cukup menggunakan string kosong di tengah + " " +
# maka output nya akan menambahkan spasi
print('Output menggunakan string concatenate dengan +"..."+')
nama_lengkap = nama_pertama +" "+ nama_tengah + "'" + nama_akhir
print(nama_lengkap)

print('\n===================================================\n')

# (2. Menghitung Panjang string) menggunakan  len(nama_lengkap)
# Hasil dari variabel nama_lengkap maka akan dihitung dan akan ditampilkan di terminal dan spasi akan tetap terhitung  

print("Menghitung panjang string")
panjang = len(nama_lengkap)

#print("Panjang dari" + nama_lengkap + "=" +(panjang))
# membuat ouput diatas akan menghasilkan eror  TypeError: can only concatenate str (not "int") to  str
# karena harus di konversi ke str terlebih dahulu 
# contoh yang benar
print("Panjang dari " + nama_lengkap + " = " +  str(panjang))

print('\n===================================================\n')


# (3. Operator untuk string)

# Mengecek apakah ada komponen char atau string di string
# menggunakan in dan not in str(variabel) 
print("Mengecek apakah string ucup didalam variabel nama_lengkap")
d = "ucup"
status = d in nama_lengkap
# mengecek apakah ada char d didalam variabel nama_lengkap
# tidak ada karena huruf d di dalam variabel nama_lengkap adalah D jadi false
print(d + " ada di " + nama_lengkap + " = " + str(status))
# output string dalam print ini jika ada spasi maka output nya juga memberikan spasi 


# d
print("Mengecek apakah string d ada di variabel nama_lengkap")
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))


# D
print("Mengecek apakah string D ada didalam variabel nama_lengkap")
D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

# d
# not in
print("Mengecek apakah string d tidak masuk di dalam variabel nama_lengkap")
d = d
status = d  not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

print('\n===================================================\n')

# Mengulang string
print("Mengulang string")

# akan membuat wk menjadi 10 kali 
print("wk"*10)
print(10*"wk") # atau membuat nya terbalik tetep bisa

# menit 10.50
print('\n===================================================\n')


# indexing
# contoh menggunakan indexing [0]
# output nya menjadi suatu isi nilai dari variabel nama_lengkap tergantung angka yang 
# dipilih

# [0 1 2 3 4 5 6] itu karakter awal dari akhir 
# [-0 -1 -2 -3 -4 -5 -6] itu karakter akhir ke awal atau karakter dari belakang
print("\nindexing menggunakan [0] sampai dengan [6]\n")
print("isi dari variabel nama_lengkap = ",nama_lengkap)
print("index ke ->0 = " + nama_lengkap[0]) # u
print("index ke ->1 = " + nama_lengkap[1]) # c
print("index ke ->2 = " + nama_lengkap[2]) # c
print("index ke ->3 = " + nama_lengkap[3]) # u
print("index ke ->4 = " + nama_lengkap[4]) # p
print("index ke ->5 = " + nama_lengkap[5]) # ini spasi kosong
print("index ke ->6 = " + nama_lengkap[6]) # '

# penggunaan index harus sesuai isi nilai dari variabel jika sudah tidak ada variabel yang terprint maka akan menghasilkan eror 

# contoh menggunakan indexing [-0]
print('\nindexing menggunakan [-0] sampai dengan [-6]\n')
print("isi dari variabel nama_lengkap = ",nama_lengkap)
print("index ke ->(-0) = " + nama_lengkap[-0]) # sama aja kek output = u
print("index ke ->(-1) = " + nama_lengkap[-1])
print("index ke ->(-2) = " + nama_lengkap[-2])
print("index ke ->(-3) = " + nama_lengkap[-3])
print("index ke ->(-4) = " + nama_lengkap[-4])
print("index ke ->(-5) = " + nama_lengkap[-5])
print("index ke ->(-6) = " + nama_lengkap[-6])

print("\nindexing menggunakan [0:3] atau bisa menggunakan angka acak\n")
print("index ke ->[0:3] = " + nama_lengkap[0:4])
print("index ke ->[3:7] = " + nama_lengkap[3:8])
print("index ke ->[0,2,4,5,8,10] = " + nama_lengkap[0:11:2])
print('\n===================================================\n')



# item paling kecil
# menggunakan min(nama_lengkap)
# dan menggunakan max(nama_lengkap)
print("Mencari huruf a b c paling besar menggunakan min(nama_lengkap) dan max(nama_lengkap)")
print(nama_lengkap)
print("Paling kecil : " + min(nama_lengkap)) # tidak ada dikarenakan tidak ada huruf minimal kek abc
print("paling besar : " + max(nama_lengkap)) # output u karena abc sampe u huruf u adalah yang terbesar
print('\n===================================================\n')


# ascii_code
# menentukan nilai ascii dari suatu nilai variabel
# menggunakan str(ascii_code)
# menentukan ascii dari double quote " "

# kalau data nya string kek dibawah harus menggunakan str
print("Menentukan nilai ascii_code menggunakan ord() dan chr() dan str()")
ascii_code = ord(" ") # Konversi karakter ke angka ASCII
print("char untuk ASCII 117 adalah = " + str(ascii_code))

# menggunakan chr(data)
# kalau data nya int seperti dibawah harus menggunakan chr()
data = 117
print("char untuk ASCII 117 adalah = " + chr(data)) # Konversi angka ASCII ke karakter
print('\n===================================================\n')
# kedua kode diatas sebenar nya tidak membuat eror jika diganti 


# 4. Operator dalam bentuk method menggunakan variabel.count("huruf variabel")
# Menghitung o didalam variabel
data = "pocong bencong kentong lontong"
print(data)
jumlah = data.count("o")
print("jumlah o pada variabel pada " + data + " = " + str(jumlah))
print('\n===================================================\n')
