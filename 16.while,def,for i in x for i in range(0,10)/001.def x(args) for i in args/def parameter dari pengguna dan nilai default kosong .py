# ==============================================
# FUNGSI DENGAN PARAMETER WAJIB DARI PENGGUNA
# ==============================================

def test(nama, kelas, tempattinggal):                     # Definisi fungsi dengan 3 parameter wajib
    print("nama anda :", nama)                            # Menampilkan nama yang diinput
    print("kelas :", kelas)                               # Menampilkan kelas yang diinput
    print("tinggal di:", tempattinggal)                   # Menampilkan tempat tinggal yang diinput

test(nama="radit", kelas='12', tempattinggal="bakung")    # Pemanggilan fungsi dengan keyword arguments
print("=" * 50)                                           # Cetak garis pemisah di output


# ==============================================
# FUNGSI DENGAN PARAMETER NILAI DEFAULT
# ==============================================

def test2(nama='', umur='', tempattinggal=''):            # Definisi fungsi dengan nilai default kosong ('')
    print('nama saya :', nama)                            # Menampilkan nama
    print('umur saya :', umur)                            # Menampilkan umur
    print('tempat :', tempattinggal)                      # Menampilkan tempat tinggal

test2('radit', 18, 'jambi')                               # Pemanggilan fungsi dengan positional arguments
