# operasi komparasi

# setiap hasil dari komparasi adalah boolean

# yang berarti true atau false
# macam operasi aritmatika
# < > <= >= == != is is not


a = 4
b = 2

# lebih besar dari >
# menentukan nilai terbesar dari nilai variabel a dan b
print("hasil besar dari >")
hasil = a > 3
print(a, ">",3, "=", hasil)
hasil = b > 3
print(b, ">",3, "=", hasil)
hasil = b > 2
print(b, ">",2, "=", hasil) # dalam python kenapa 2 > 2 adalah False karena 2 tidak lebih besar dari 2




# lebih kecil kurang dari <
# menentukan nilai kecil dari , dari nilai variabel a dan b
print("hasil kecil dari <")
hasil = a < 3
print(a, "<",3, "=", hasil)
hasil = b < 3
print(b, "<",3, "=", hasil)
hasil = b > 2
print(b, "<",2, "=", hasil)


# lebih besar sama dengan >=
#
print("hasil lebih dari  sama dengan >=")
hasil = a >= 3
print(a, ">=",3, "=", hasil)
hasil = b >= 3
print(b, ">=",3, "=", hasil)
hasil = b >= 2
print(b, ">=",2, "=", hasil)

# lebih kecil sama dengan <=
print("hasil lebih kecil sama dengan <=")
hasil = a <= 3
print(a, "<=",3, "=", hasil)
hasil = b <= 3
print(b, "<=",3, "=", hasil)
hasil = b <= 2
print(b, "<=",2, "=", hasil)

# hasil sama dengan ==
print("hasil sama dengan ==")
hasil = a == 4
print(a,"==",4, "=", hasil)
hasil = b == 4
print(b,"==",4, "=", hasil)
# operator ini mengecek apakah nilai dari variabel a sama dengan 4 atau tidak kalau iya
# maka hasilnya True kalau tidak maka False

# hasil sama dengan !=
# != artinya tidak sama dengan
print("hasil sama dengan !=")
hasil = a != 4
print(a,"!=",4, "=", hasil)
hasil = b != 4
print(b,"!=",4, "=", hasil)


# is sebagai komperasi object identy
print("object identity is")
x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(x)))
hasil = x is y # disini karena dia true karena x dan y adalah 5
print(x, "is", y, "=", hasil)

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(x)))
hasil = x is y # disini karena dia false karena x dan y adalah 5 dan 6
print(x, "is", y, "=", hasil)

print("object identity is not")
x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(x)))
hasil = x is not y
print(x, "is", y, "=", hasil)

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(x)))
hasil = x is not y
print(x, "is", y, "=", hasil)
