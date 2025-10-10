# Contoh sederhana penggunaan perulangan while

x = 1  # Inisialisasi variabel x dengan nilai awal 1

# Perulangan akan terus berjalan selama nilai x kurang dari 10
while x < 10:
    print(x)       # Menampilkan nilai x ke layar
    x = x + 1      # Menambah nilai x sebesar 1 setiap kali perulangan
                   # Supaya nilai x terus berubah dan perulangan bisa berhenti saat x >= 10
# maka kode berjalan dari 1 sampai 9 


print("="*50)


# contoh kedua penggunaan dalam string 
x = "radit"
while x:
    print(x)
# 💀 peringatan kode ini akan terus berjalan dan tidak akan berhenti
# maka fungsi break agar tidak mengeluarkan output berlebih
# pencet ctrl + c untuk berhenti