# class dalam python 
class A:                            # class pertama yaitu A
    print("ini adalah class A")     # output 
    attr1 = "ini adalah attr1"      # variabel dengan isi string
    print(attr1)
    def fungsi(self):               # self = penunjuk ke objek itu sendiri, dipakai untuk akses atribut dan method dalam class
        print("ini adalah fungsi")  # output

print("\noutput\n")

# pemanggilan  A
a = A() # pemanggilan dari class variabel A
print(a) # output dari A akan berupa sebuah kode didalam terminal 

# pemanggilan attr1 
a.attr1
print(a)

# pemanggilan fungsi 
a.fungsi
print(a)



# kode ini berfungsi untuk consol kode diatas hanya contoh dibuat 

#class A:
#    'INI CLASS A'
#     attr = 'ini attr'
#     def function(self):
#             "ini function"

# untuk pemanggilan di consol 
# a =A()      pemanggilan A dalam kode 
# a.fungsi()  pemanggilan function 
# A.__doc__   pemanggilan isi dari A


