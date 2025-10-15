# belajar function 
# aturan *args bisa menjadi tuple ketika nilai variabel 
# menjadi string koma "",""
# *args bisa digunakan dalam dua argumen entah itu int atau string


def f2(*args): 
    for i in args:
        print(i)
a1 = "bahasa python","pembuuat","Guuido van rosuum"

f2(a1) # dan pembuatan variabel harus seperti ini tidak dengan f2 =(a1) dan di ikuti nama function 
print(f2) # output akan menjadi sebuah list() 

print("="*50)

# fungsi menggunakan (*args)

def fungsi(*args):
    for i in args:
        print(i)
nama = "Radit"
umur = 18
fungsi('halo nama aku ' ,nama, 'umur ku ',umur)

print("="*50)
