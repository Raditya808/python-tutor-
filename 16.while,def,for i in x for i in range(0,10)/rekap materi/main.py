# function menggunakan *args
# *args berfungsi menerima dua argumen dan bisa menjadi tuple dalam python 
# contoh dibawah menerima dua argumen dalam str dan int 

print("="*50)
print("Penggunaan *args dalam dua argumen int dan str")

def argstes(*args):
    for i in args:
        print(i)

a = "Radit"
b = 18 
argstes(a,b)


# print perulangan 
print("="*50)


# contoh dalam penggunaan tuple 
print("Penggunaan *args dalam string")
def list(*args):
    for i in args:
        print(i)
a = "Muhammad","Raditya","Ramadhan"
list(a)

print("="*50)

print("Lopping satu sampai 9 seperti while")
for i in range(0,10):
    print(i)
    



print("="*50)

print("Belajar looping menggunakan while")
# belajar while 
# while dalam kondisi looping berhenti 
a = 1 
while a<10:
    print(a)
    a = a + 1 
# maka output nya sampai 9 

# HATI HATI KONDISI LOOPING JIKA MENGGUNAKAN SYNTAX KEK GINI
# MAKA AKAN TERUS BERJALAN 
# a = 1 
# while a:
    #print(a)

print("="*50)

# contoh looping while menggunakan break  
print("Kondisi while ketika menggunakan break")
a = 1  
while a<200:
    print(a)
    a = a + 1 # bagian ini jika salah satu variabel di tambah satu maka akan setiap output yanng keluar 
              # maka akan output yang keluar akan terstruktur
    break # fungsi break akan mengeluarkan output variabel x/ menghentikan looping
            # karena break akan hanya mengeluarkan output x 
print("="*50)

# tidak menggunakan break 
print("Tidak menggunakan break")
a = 1 
while a <200:
    print(a)
    a = a + 1
print("="*50)

# penggunaan else jika tidak ada looping 
print("Penggunaan else")
a = 1 
while a <200:
    print(a)
    a = a + 1 
else:
    print("selesai")
print("="*50)

# penggunaan if statement 
print("Pengunaan if dan else")
a = 1 
while a:
    if a <10 :
        print(a)
        a = a + 1
else:
    print("selesai")
