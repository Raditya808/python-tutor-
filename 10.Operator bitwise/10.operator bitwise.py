# operator bitwise

# atau operasi binner
# Bitwise = operasi yang dilakukan pada masing-masing bit dari bilangan biner.
#
# “Bit” adalah digit terkecil dalam representasi biner, yaitu 0 atau 1.
#
# Bitwise bekerja langsung pada bentuk biner, bukan pada nilai desimalnya.

# bitwise ---> operasi masing masing bit

# misal

# int --> 2  00000010
#     index  76543210
#           2 pangkat 1 dikarenakan o itu adalah dua dan karena index nya 1 maka 2 pangkat 1
'''----------------------'''
# int --> 1 00000001
#           2 pangkat 0 = 1
# Bit paling kanan (index 0) bernilai 1.
#
# Nilainya adalah 2 pangkat 0 = 1.

'''----------------------'''
# int --> 9 --> 00001001
# -->           2 pangkat 3 = 8
# -->           2 pamgkat 0 = 1
# dijumlahkan maka hasil nya 9
'''-----------------------'''
# lalu hasil angka int tadi di or kan
# 2 or 1 --> 2 --> 0000010
#            1 --> 0000001
#            --------------
#                  0000011
'''-----------------------'''
# = 2 pangkat 1 = 2
# = 2 pangkat 0 = 1
# hasil nya = 3
#######################################################################


# contoh variabel
a = 9
b = 5


# bitwise or (|)
c = a | b
print('\n====================OR====================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('-----------------(\)----------------------')
print('nilai :',c,'binary :',format(c,'08b'))
# maksud daei 08b adalah memformat angka nilai dari variabel menjadi 8 angka menjadi 0
# maka hasil nya 00001001

# bitwise AND (&)
c = a & b
print('\n====================AND===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('-----------------(&)----------------------')
print('nilai :',c,'binary :',format(c,'08b'))

# bitwise XOR (^) 
c = a ^ b
print('\n====================XOR===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('-----------------(^)----------------------')
print('nilai :',c,'binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n====================NOT===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('-----------------(~)----------------------')
print('nilai :',c,'binary :',format(c,'08b'))
print('---------------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,'binary : ',format(e^d,'08b'))

# shifting

# shifting right (>>)
c = a >> 2
print('\n====================>>===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('-----------------(~)----------------------')
print('nilai :',c,'binary :',format(c,'08b'))
print('---------------------------------------(>>)')

# shifting left (<<)
c = a << 2
print('\n====================>>===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('-----------------(~)----------------------')
print('nilai :',c,'binary :',format(c,'08b'))
print('---------------------------------------(>>)')

print("\n=====================================================================================================\n")
print("bawah contoh kode sendiri ")
print("\n=====================================================================================================\n")

# contoh kode sendiri
#bitwise code 
a = 9
b = 5

# hasil dari operator bitwise dalam bentuk output dan hasil dari angka yang akan di eksekusi 
# opeartor ini menggunakan operator bitwise tapi bentuk sederhama

# contoh kode menggunakan operator bitwise dalam bentuk 
# bitwise or atau ( | )

  # 1001   (9)
  # 0010   (2)
  # ----
  # 1011   (hasil)

# macam macam opeatoor yaitu xor ( ^ ), and ( & ), or ( | ), not ( ~ ), shifting right ( >> ), shifting left ( << )
print('nilai a =',a)
print('nilai b =',b)

# operator bitwise dari or atau logo nya ( | )
print('\n====================OR====================\n')
c = a | b
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('nilai variabel OR a | b =',c,'nilai binary = ', format(c,'08b'))
# contoh opeartor jika menggunakan format string
print('---------------------------------------( | )')   


# operator bitwise dari and atau logo nya (&)
print('\n====================AND===================\n')
c = a & b # operator and
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('nilai variabel AND a & b =',c,'nilai binary = ', format(c,'08b'))
print('---------------------------------------( & )')
# contoh opeartor jika menggunakan format string
# contoh  opeartor jika tidak menggunakan menggunakan atau tidak menggunakan format


# operator bitwise dari xor atau logo nya (^)
print('\n====================XOR===================\n')
c = a ^ b
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('nilai variabel XOR a ^ b =',c,'nilai binary = ', format(c,'08b'))
print('-------------------------------------------(^)')

# operator bitwise dari not atau logo nya (~)
c = ~a
print('\n====================NOT===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('nilai variabel NOT a ~ b =',c,'nilai binary = ', format(c,'08b'))
print('-------------------------------------------------------( ~ )')

# konversi nilai ke desimal metode xor
d = 0b0000001001
e = 0b1111111111
# print metode cepat
print('nilai dari d^e =',d^e,'nilai binary =',format(d^e,'08b'))
print('-------------------------------------------------------( ~ )')


# shifting left >>
c = a >> 2
print('\n==================== SHIFTING LEFT >> ===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary',format(b,'08b'))
print('\n==================== SHIFTING LEFT >> ===================\n')

# shifting right <<
c = a << 2
print('\n==================== SHIFTING RIGHT << ===================\n')
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
print('\n==================== SHIFTING RIGHT << ===================\n')





