# operasi bolean

# not , or , and, xor

print("----------not-------")
a = False
c = not a
print('data a',a)
print('data c',c)
print("--------------------")
# sederhana dari kode ini 
# not false --> True
# not true --> False

# OR
# khusus (or) jika salah satu nilai variabel adalaah True maka hasilnya True
print("----------Or----------")
a = False
b = False
c = a or b
print(a, 'OR' ,b,'=',c)
a = False
b = True
c = a or b
print(a, 'OR' ,b,'=',c)
a = True
b = False
c = a or b
print(a, 'OR' ,b,'=',c)
a = True
b = True
c = a or b
print(a, 'OR' ,b,'=',c)
print("--------------------")

# AND
# khusus (and) jika dua buah nilai variabel adalah True maka hasilnya True
print("----------and----------")
a = False
b = False
c = a and b
print(a, 'AND' ,b,'=',c)
a = False
b = True
c = a and b
print(a, 'AND' ,b,'=',c)
a = True
b = False
c = a and b
print(a, 'AND' ,b,'=',c)
a = True
b = True
c = a and b
print(a, 'AND' ,b,'=',c)
print("--------------------")

# XOR
# adalah operator bitwise
# akan true jika salah satu nilai variabel adalah True sisanya false
print("----------xor----------")
a = False
b = False
c = a ^ b
print(a, 'XOR' ,b,'=',c)
a = False
b = True
c = a ^ b
print(a, 'XOR' ,b,'=',c)
a = True
b = False
c = a ^ b
print(a, 'XOR' ,b,'=',c)
a = True
b = True
c = a ^ b
print(a, 'XOR' ,b,'=',c)
print("--------------------")
