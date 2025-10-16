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