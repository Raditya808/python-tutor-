# casting adalah mengubah tipe data ke tipe data lain

# macam macam tipe data
# int
# float
# str
# bool


# variabel output integer
from traceback import print_tb


print("INTGER")
data_int = 9;
print("data =", data_int,"type =", type(data_int)) # output int

# menggabungkan variabel = 9 diatas dan memanipulasi tipe data sebagai int , str , bool
# int adalah tipe data bilangan bulat
# float adalah tipe data bilangan pecahan
# str adalah tipe data string (teks)
# bool adalah tipe data boolean (True/False)

data_float = float(data_int) # variabel sebagai tipe data float
data_str   = str(data_int) # variabel sebagai tipe data string
data_bool  = bool(data_int) # variabel sebagai tipe data boolean # jika angka nya 0 maka False, selain itu True

# dibawah adalah output dari variabel yang sudah diubah tipe datanya
print("data =", data_float,"type =", type(data_float))
print("data =", data_str,"type =", type(data_str))
print("data =", data_bool,"type =", type(data_bool))

"""================================================================="""
print("==================================================================")

# variabel output float
print("FLOAT")
data_float = 0;
print("data =", data_float,"type =", type(data_float))

data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)

print("data =", data_int,"type =", type(data_int))
print("data =", data_str,"type =", type(data_str))
print("data =", data_bool,"type =", type(data_bool))

print("==================================================================")

print("BOOL")
data_bool = False;
print("data =", data_bool,"type =", type(data_bool))

data_int   = int(data_bool)
data_str   = str(data_bool)
data_float = float(data_bool)

print("data =", data_int,"type =", type(data_int))
print("data =", data_str,"type =", type(data_str))
print("data =", data_float,"type =", type(data_float))
print("==================================================================")

print("STRING")
data_str = "9"; # memasukan variabel ini harus berupa angka dengan str jika tidak ada nilai sama sekali maka
# akan menghasilkan error
print("data =", data_str,"type =", type(data_str))

data_int     = int(data_str)
data_bool    = float(data_str)
data_float   = bool(data_str)

print("data =", data_int,"type =", type(data_int))
print("data =", data_bool,"type =", type(data_bool))
print("data =", data_float,"type =", type(data_float))
print("==================================================================")

# contoh kode
# menggunakan tipe data integer 
print("data integer ")
data1 = 9;
print('data1 =',data1,'tipe nya adalah:',type(data1))

print("==================================================================")

# mengcasting tipe data ke tipe data lain dari int ke float
# int ke string
# int ke boolean

intkefloat = float(data1)
intkestr = str(data1)
intkebool = bool(data1)
print('data1 =',intkefloat,'tipe nya adalah:',type(intkefloat))
print('data1 =',intkestr,'tipe nya adalah:',type(intkestr))
print('data1 =',intkebool,'tipe nya adalah:',type(intkebool))

print("==================================================================")

# mengcasting tipe data float ke tipe data lain dari 
# menggunakan tipe data float
# dan mengcasting ke tipe data ke yang lainnya 
print("data float")
data2 = 0;
print('data =',data2,'tipe nya adalah:',type(data2))

# mengcasting tipe data dalam bentuk 
# float ke tipe data lain 
floatkeint = int(data2)
floatkestr = str(data2)
floatkebool = bool(data2)

# output variabel 
print('data2 =',floatkeint,'tipe nya adalah:',type(floatkeint))
print('data2 =',floatkestr,'tipe nya adalah:',type(floatkestr))
print('data2 =',floatkebool,'tipe nya adalah:',type(floatkebool))

# mengcasting tipe data string ke tipe data lain
# string 
print("data string")
data3 = "9";
stringkefloat = float(data3)
stringkeint = int(data3)
stringkebool = bool(data3)
print('data3 =',stringkefloat,'tipe nya adalah:',type(stringkefloat))
print('data3 =',stringkeint,'tipe nya adalah:',type(stringkeint))
print('data3 =',stringkebool,'tipe nya adalah:',type(stringkebool))

