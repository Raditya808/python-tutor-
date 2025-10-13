a = 0 
b = 0 
try:
    a / b # ketika ini di eksekusi karena variabel a dan b 0 maka akan eror 
except: # kode diatas adalah contoh error handling 
    print("error tidak memiliki angka")
    
    
else:
    print("tidak error karena ada angka") # jika variabel tersebut memiliki angka
    # maka line ini akan di eksekusi 