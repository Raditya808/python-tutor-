# operasi aritmatika


a = 11
b = 3

# operasi tambah +

hasil = a + b
print(a,'+', b, '=', hasil)

# operasi kurang -
hasil = a - b
print(a,'-', b, '=', hasil)

# operasi kali *

# dalam python kali bukanlah x melainkan *

hasil = a * b
print(a, '*', b, '=', hasil)

# operasi bagi atau /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponene (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus
# cara hitung nya pertama adalah di bagi
# hasil bagi nya lalu di kali dengan 3
# jadi 11 / 3 = 3.6666666666666665
# lalu 3 * 3 = 9
# lalu 11 - 9 = 2
# operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division //

hasil = a // b
print(a, '//', b,'=', hasil)


# prioritas operasi, operational precedence
'''Prioritas operasi dalam Python mengikuti aturan matematika standar:
1. Kurung ()
2. Eksponen (**)
3. Perkalian dan teman teman (*, /, //, %)
4. Pertambahan dan pengurangan (+, -)'''
x = 3
y  = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)


hasil = x + y * z
print(x , '+', y, '*', z, '=', hasil)
# kenapa hasilnya 11?
# karena operasi perkalian lebih diutamakan daripada penjumlahan
# jadi untuk mencari hasilnya adalah
# 2 * 4 = 8
# lalu 3 + 8 = 11

# kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)