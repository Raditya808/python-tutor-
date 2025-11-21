# class pewaris 
class kendaraan: # class bernama kendaraan
    def __init__(self,nama="",merk=""): # __init__ berfungsi untuk pemanggilan nama dan merk serta self untuk penamaan dari variabel tersebut
        self.nama = nama # penamaan nama dan merk menggunakan self 
        self.merk = merk

    def output(self): # output menggunakan self 
        print(self.nama) 
        print(self.merk)

# class mobil 
class mobil(kendaraan): # pemanggilan dari kendaraan agar menjadi pewaris 
    def __init__(self, nama,merk,warna): 
        super().__init__(nama, merk) # super yang berfungsi untuk pemanggilan kembali dari nama dan merk 
        self.warna = warna # penambahan data warna 

    def output(self): # output 
        print(self.nama)
        print(self.merk)
        print(self.warna)

# tes output
tes1 = mobil(nama="mobil",merk="toyota",warna="hitam")
tes1.output()
tes2 = kendaraan(nama="motor",merk="honda")
tes2.output()
