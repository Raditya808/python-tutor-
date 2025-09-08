# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3--------10+++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++++3-----------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ---------------10++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# ++++++3--------10+++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)


# -----3++++++++10--------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -----3++++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)

# +++++++++++++++10-------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ",isKurangDari)

# -----3++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)


print("\n===========\n")


# contoh kode
inputpengguna =  int(input("masukan nilai yang bernilai kurang dari 3 atau lebih besar dari 10:  "))




# memeriksa apakah angka pengguna lebih kecil dari 3
print("===============================================")
print("\nOperator OR")
inputbesardari = (inputpengguna < 3) 
print(inputpengguna,'kurang dari dari 3 =', inputbesardari)


# memeriksa apakah angka pengguna besar dari 10
inputkurangdari = (inputpengguna > 10)
print(inputpengguna,'besar dari 10 =',inputkurangdari)

# memeriksa hasil keduanya
isbenaratausalah = inputbesardari or inputbesardari
print("hasil dari keduanya: ",isbenaratausalah)
print("===============================================")

# memeriksa kedua variabel dalam or 
# disini dia akan melihat dua output yang dimana antara true atau false maka 
# akan di cek dalam bentuk or
#------------------------------------- 
# operasi OR (|)            #---------
# true  or true = (true)    #---------
# true or false = (true)    #---------
# false or true = (true)    #---------
# false or false = (false)  #---------
#-------------------------------------
# dalam or nilai true atau false hasil nya tetap akan true
# kecuali false or false
# mengecek or






print("\nOperator AND")
# memeriksa apakah angka pengguna lebih kecil dari angka 3
inputbesardari = (inputpengguna > 3)
print(inputpengguna,'besar dari 3 =',inputbesardari)


# memeriksa apakah pengguna lebih besar dari 10
inputkurangdari = (inputpengguna < 10)
print(inputpengguna,'kecil dari 10 =',inputkurangdari)

# memeriksa hasil keduanya
isbenaratausalah = inputbesardari and inputkurangdari
print("hasil dari keduanya: ",isbenaratausalah)
print("===============================================")

#------------------------------------
# operasi AND (&)           #--------
# true & true = true        #--------
# true & false = false      #--------
# false & true = false      #--------
# false & false = false     #--------
#------------------------------------




