# pengenalan string

# string adalah kumpulan karakter karakter didalam tanda petik


# mengatahui sebuah tipe data didalam variabel
# string double quote ""
print('"ini adalah menentukan tipe data string dengan double quote"')
print("=======================================================================")     
data = "string double quote"                                              #=====
                                                                          #=====
print(data)                                                               #=====
                                                                          #=====
# mengatahui kalau itu bertipe string menggunakan type                    #=====
# tergantung tipe data nya juga kalau int atau float maka memasukan angka #=====
                                                                          #=====
print(data,"tipe nya adalah:",type(data))                                 #=====
print("=======================================================================")

# 1. cara membuat string
# menggunakan ''' '''

'''
    1. membuat string dengan single quote '...'
    2. membuat string dengan double quote "..."

'''

# mengatahui sebuah tipe data didalam variabel
# string dalam single quote ''
print("'ini adalah menentukan tipe data string dengan single quote'")
print('=======================================================================')
data = 'string single quote'                                              #=====
                                                                          #=====
print(data)                                                               #=====
                                                                          #=====
# mengatahui kalau itu bertipe string menggunakan type                    #=====
# tergantung tipe data nya juga kalau int atau float maka memasukan angka #=====
                                                                          #=====
print(data,'tipe nya adalah:',type(data))                                 #=====
print('=======================================================================')

# dalam python penggunaa string seperti ini
# print('" akan tetap tereksekusi karena penutupan string masih jelas "')

# tetapi menggunakan string seperti ini print('" ") menghasilkan eror string literal
# akan terjadi eror dikarenakan penutupan tanda '' yang tidak jelas

print("\ncontoh penggunaan string single quote dan double quote\n")
print('=======================================================================')
print('"ini akan menampilkan string double quote nya"')             #==========
print("'ini akan menampilkan string single quote nya'")             #==========
print("ini adalah hari jum'at")                                     #==========
print('=======================================================================')

# dalam kode diatas penggunaan single quote dalam kata jum'at tidak menghasilkan eror sama sekali dikarenakan penutup nya double quote yang jelas sehingga tetap ditmapilkan di terminal



# 2. Menggunakan string dengan tanda slash \

# membuat tanda ' menjadi string menggunakan \

# contoh kode
print('\npenggunaan string tanda petik dua kali\n')
print('=======================================================================')
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')
print('=======================================================================')

# backslash
print("\n\\\\ penggunaan backslash dua kali\n")
print('=======================================================================')
print("c:\\user\\ucup")
# penggunaan \ dua kali akan membuat salah satu nya menjadi komentar
print('=======================================================================')

# tab 
# tab menggunakan \t\t
print('=======================================================================')
print("ucup\t\t\totong, jauan")
print('=======================================================================')

# backspace 
# membuat teks menjadi berdekatan menggunakan \b
print('=======================================================================')
print("ucup dan \botong, jadi deketan")
print('=======================================================================')

# newline
# membuat newline / meng enterkan  menggunakan \n
print('=======================================================================')
print("baris pertama. \nbaris kedua.") # LF --> line feed --> unix, linux
print("baris pertama. \rbaris kedua.") # CR --> carriage return --> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF --> line feef carriage return --> dipakai oleh windows
print('=======================================================================')

# 3. String literal atau raw 
# hati-hati
print('=======================================================================')
print('C:\newfolder') # path yang salah karena n dijadikan escpae secuence untuk line baru
print('C:\nnewfolder') # path yang benar ini tetap nampil tapi bagaimana jika slash nya akan banyak ? yaitu menggunakan raw
print('=======================================================================')

# raw string menggunakan (r'..')
# atau bisa menggunakan tab (\t)
# menggunakan backspace (\b)
print('=======================================================================')
print(r'C:\new \t\r\b\\folder')
print('=======================================================================')

# multiline untuk literal string """..."""
# contoh kode
print('=======================================================================')
print(""" 
Nama : ucup
kelas : 10
""")
print('=======================================================================')

# multiline literal string dan RAW 
print('=======================================================================')
print(r"""
Nama : ucup 
kelas : 3 SMP\new normal
website : www.ucup.com/newID
""")
print('\n=======================================================================\n')

# ver sendiri
# tata cara penggunaan string 
# 1. menggunakan single quote dalam bentuk komentar
'''
ini adalah string single quote dan tidak akan tereksekusi di terminal

'''

# atau bisa menggunakan double quote dalam bentuk komentar

"""
atau bisa menggunakan double quote
"""

# 2. penggunaan string dalam single quote ('') dan menghasilkan output dalam terminal 
data_singlequote = 'ini adalah string single quote'

print(data_singlequote,'tipe nya adalah :',type(data_singlequote))


data_doublequote = "ini adalah string double quote"

print(data_doublequote,"tipe nya adalah :",type(data_doublequote))
# di kedua kode ini tidak akan jauh berbeda sebenarnya keduanya tetap kebaca string di terminal dan akan tetap begitu selama ada tanda "" dan ''
print('\n=======================================================================\n')

# 3. contoh penggunaan string single dan double quote ketika ada salah salah satu variabel nya ada ''
# atau penggunaan penutup "'...'" atau '"..."'

print("'halo cui'") # menampilkan single quote
# ini akan tereksekusi di terminal karena penutup tag nya yang jelas
# begitu juga sebalik nya 
print('"halo cui"') # menampilkan double quote

# print('halo cui'")
# jika penggunaan string nya seperti kode diatas maka akan menghasilkan eror karena penutup tag yang tidak jelas

#=====================================================================================
# print('hari jum'at')
# begitu pula jika penutup titik nya seperti ini maka akan eror begitu juga sebaliknya 
# print("hari jum"at")
#=====================================================================================

print('\n=======================================================================\n')



# 4. string slash \
print('sir\'good life\'isnt')
# atau 
print('hari jum\'at')
# maka ini akan menampilkan tanda kutip juga dan dianggap sebagai string
print('\n=======================================================================\n')

# penggunaan backslash \ 
print('c:\\inifile\\lmaonigga')
# penggunaan backslash \ dua kali akan membuat salah satunya menjadi string dan tidak akan kebaca di terminal 

# atau contoh kedua menggunakan double quote ".."
print("c:\\inifile\\lmaonigga") 
# keduanya tetap menampil di terminal 
print('\n=======================================================================\n')

# tab menggunakan \t dengan slash
# fungsi slash \t adalah mengtab kan variabel di dalam print
print('halo\t\tapa kabar')

print('\n=======================================================================\n')

# menggunakan \b backspace membuat teks menhjadi berdekatan
print('halo \bradit apa kabar')
# menggunakan slash b \b akan membuat suatu teks menjadi berdekatan meskipun ada spasi 
print('\n=======================================================================\n')

# newline / mengenterkan suatu teks menggunakan \n 
print('apa \nkabar') # teks tersebut akan ter enterkan
print('\n=======================================================================\n')

# aturan string ketika menggunakan slash
print('\nona manis') # path n bukan menjadi teks melainkan menjadi karakter escape secuence ke line baru

# maka yang benar yaitu 
print('\nnona manis')
print('\n=======================================================================\n')

# raw string menggunakan r".."
# akan menampilkan semua karakter menjadi string bahkan jika ada kelebihan karakter sekalipun
print(r'C:\\inifile\\lmaonigga\\')
print(r'C:\inifile\r\t\\p\l\ppppp\\')
print('\n=======================================================================\n')

