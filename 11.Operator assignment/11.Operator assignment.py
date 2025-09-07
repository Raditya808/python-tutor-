# operator assignment
# operasi yang dapat dilakukan dengan penyingkatan 

# contoh 
a = 5 # ini adalah assignment
print('nilai :',a)
a += 1 # atau bisa juga seperti ini
print('nilai a += 1,nilai a menjadi ',a)
# ini adalah langkah pertama


# output 
a -= 2 
print("nilai a -= 2, nilai a menjadi ",a)
# langkah ke dua
# langkah pertama tadi hasil nya = 6
# maka 6 - 2 maka = 4

a *= 5
print("nilai a *= 5, nilai a menjadi ",a)
# ini adalah langka ketiga
# operator ini mengeluarkan output secara beruntun
# yang tadinya 4 maka 4 x 5 = 20

a /= 2
print("nilai a /= 2, nilai a menjadi ",a)
# ini adalah langkah ke empat 
# maka 20 /= 2 = 10 outputnya mengeluarkan tipe float maka menjadi 10.00

# ==========================================================================





# operator modulus
# modulus ngambil sisa pembagian
b = 10 # nilai dari variabel
print("\nnilai b :",b)


# modulus dan floor division
# output dari operasi modulus
b %=3 # 
print("nilai b %= 3, nilai b menjadi ",b)
# 10 %= 3 = 1


# operator floor division
print("\nnilai b : 10")
b = 10
b //= 3
print("nilai b //= 3, nilai b menjadi",b)

# operasi pangkat **=
a = 5
print("\nnilai a :",a)

# output 
a **= 3 
print("nilai a **= 3, nilai a menjadi",a)

print("\n===========================================")




#---------------------------------------
# Operasi bitwise 
# OR (|)
# true  | true  = 1 | 1 = 1  (true)
# true  | false = 1 | 0 = 1  (true)
# false | true  = 0 | 1 = 1  (true)
# false | false = 0 | 0 = 0  (false)
#---------------------------------------
print("\n|")
c = True  
print("\nnilai c :",c) 
c |= False # OR
print("nilai c |= False, nilai c menjadi",c)
c = False
print("nilai c :",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)


# Seluruh kode ini adalah print beruntun kebawah


#---------------------------------------
# AND (%)
# true  & true  = 1 & 1 = 1  (true)
# true  & false = 1 & 0 = 0  (false)
# false & true  = 0 & 1 = 0  (false)
# false & false = 0 & 0 = 0  (false)
#---------------------------------------
print("\n&")
c = True  
print("\nnilai c :",c) 
c &= False # AND
print("nilai c &= False, nilai c menjadi",c)
c = False
print("nilai c :",c)
c &= True
print("nilai c &= True, nilai c menjadi",c)



#---------------------------------------
# true  ^ true  = 1 ^ 1 = 0  (false)
# true  ^ false = 1 ^ 0 = 1  (true)
# false ^ true  = 0 ^ 1 = 1  (true)
# false ^ false = 0 ^ 0 = 0  (false)
#---------------------------------------
# XOR (^)
print("\n^")
c = True 
print("\nnilai c :",c)
c ^= False 
print("nilai c ^= False, nilai c menjadi",c)
c = False
print("nilai c :",c)
c ^= True
print("\nilai c ^= True, nilai c menjadi",c)
print("\n===========================================")


# geser geser
# right bitwise (>>=)
print("\nkanan")
d = 0b0100
print("nilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",d)

# left bitwise (<<==)
print("\nkiri")
d = 0b0100
print("nilai d =",format(d,'04b'))
d  <<= 1
print("nilai d <<= 1, nilai d menjadi",d)
print("\n==============================================\n")


print("\n==========Versi Kode sendiri==========\n")

 # operasi assignment
# menghitung variabel secara beruntun

print("\n==============================================\n")
print("\nMengeluarkan nilai secara beruntun\n")
a = 9
print('nilai a adalah',a)

# output assignment
# langkah ke 1 yaitu pertambahan
a += 1 
print('nilai a += 1 =',a)

a -= 2
print('nilai a -= 2 =',a)
# langkah ke 2 kurang
# perhitungan 10 -= 2 = 10 - 2 = 8

a *= 4
print('nilai a *= 4 =',a)
# langkah ke 3 kali 
# perhitungan berlanjut 8 *= 4 = 8 x 4 = 32

a /= 5
print('nilai a /= 5 =',a)
# langkah ke 4 pembagian
# perhitungan berlanjut 32 /= 5 = 32 / 5 = 6.4
print("\n==============================================\n")

# Operasi modulus
print("\nOperasi modulus\n")
b = 10 
print("\nnilai b =",b)

# modulus assignment
b %= 3
print("nilai b %= 3 =",b)


print("\n==============================================\n")
 # operasi floor division
print("\noperasi floor division\n")
b = 10 
print('nilai b =',b)

# output
b //= 3
print("nilai b //= 3 =",b)
print("\n==============================================\n")

# operasi pangkat
# **=
print("\nOperasi pangkat\n")
a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 3 =",a)
print("\n==============================================\n")

# operasi bitwise
# OR, AND ,XOR
# OR ( | )
print("\n==============================================\n")
print("\nOperator OR ( | )\n")
c = True
print('nilai c = ',c)
c |= False
print('nilai c |= False =',c)
c = False
print('nilai c = ',c)
c |= False
print('nilai c |= False =',c)
print("\n==============================================\n")

# AND (&)
print("\n==============================================\n")
print('\nOperator AND (&)\n')
c = True
print('nilai c = ',c)
c &= False
print('nilai c &= False =',c)
c = False
print('nilai c = ',c)
c &= False
print('nilai c &= False =',c)
print("\n==============================================\n")

# XOR (^)
print("\n==============================================\n")
print('\nOperator XOR (^)\n')
c = True
print('nilai c = ',c)
c ^= False
print('nilai c ^= False =',c)
c = False
print('nilai c = ',c)
c ^= False
print('nilai c ^= False =',c)
print("\n==============================================\n")

# operator geser geser 
# right bitwise >>
print("\n==============================================\n")
print('OPERATOR SHIFTING')
print('\nRight bitwise >>=')
d = 0b0100 
print('nilai d =',format(d,'04b'))
d  >>= 2
print('nilai d >>= 2 nilai d menjadi =',d)
print("\n==============================================\n")


# operator geser geser 
# left bitwise <<
print("\n==============================================\n")
print('OPERATOR SHIFTING')
print('\nRight bitwise <<=')
d = 0b0100 
print('nilai d =',format(d,'04b'))
d  <<= 1
print('nilai d >>= 2 nilai d menjadi =',d)
print("\n==============================================\n")
