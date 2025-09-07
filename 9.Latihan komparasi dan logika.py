''' latihan logika dan komparasi '''


''' gabungan area rentang dari angka '''


# ++++++3------10++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n: "))
print("--------------------")

#++++++3--------
'''memeriksa apakah variabel inputuser kurang dari 3'''
iskurangdari = (inputUser < 3)
print("kurang dari 3 =",iskurangdari)


# -------10++++++
'''memeriksa apakah variabel inputuser lebih besar dari 10'''
isbesardari = (inputUser > 10)
print("lebih dari 10 =",isbesardari)

# ++++++3------10++++++
''' menggunakan metode penggabungan dengan OR '''
''' dalam operasi logika OR jika salah satu true maka hasilnya true '''

# metode penggabungan dengan menggunakan or
ishasil = iskurangdari or isbesardari
print("hasil penggabungan keduanya dalam bentuk or =",ishasil)
print("--------------------")

print("===================================================")

# --------3+++++++10--------
'''kasus irisan'''

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n: "))

print("--------------------")
#--------3++++++++++++++++++
islebihdari = inputUser > 3
print("lebih dari 3 = ",islebihdari)


# +++++++++++++++10----------
# kurang dari 10
iskurangdari = inputUser < 10
print("kurang dari 10 =",iskurangdari)
print("--------------------")

# ------3++++++++++10--------
ishasil = iskurangdari and islebihdari
print("hasil penggabungan keduanya dalam bentuk and =",ishasil)


''' PPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'''

inputuser1 = float(input("masukan angka yang anda pilih: "))

# +++++++0++++++5
hasil1 = inputuser1 > 0
hasil2 = inputuser1 < 5
print("hasil input user1 = ",hasil1)
print("hasil input user2 = ",hasil1)

