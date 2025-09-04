""" VARIABEL """
""" Variabel adalah tempat untuk menyimpan data dalam program."""
""" dalam python variabel itu adalah a """
""" dan = itu adalah operator assignment """
""" 10 itu adalah nilai dari variabel a """

a = 10
x = 5
panjang = 1000


print("nilai a adalah = ", a)
print("nilai x adalah = ", x)
print("nilai panjang adalah = ", panjang)

print("==========================")
# dalam penggunaan variabel tidak boleh ada spasi mesti dikasih underscore
# membuat variabel seperti ini  (nilai a = 10) itu salah karnea akan ada eror

# penamaan variabel

nilai_y = 20 # ini benar karena menggunakan underscore
#10_juta = 10000000  # ini salah karena tidak boleh diawali dengan angka dan akan eror
# mestinya seperti ini
juta10 = 10000000  # ini benar karena tidak diawali dengan angka
print("nilai juta10 adalah = ", juta10)
print("nilai y adalah = ", nilai_y)


print("==========================")

# memanggil nilai variabel dengan flask package

from flask import Flask

app = Flask(__name__)

@app.route('/')
def mengenal_variabel():
    return f"""
    <h1>Belajar Variabel</h1>
    <p>Nilai a adalah: {a}</p>
    <p>Nilai x adalah: {x}</p>
    <p>Nilai panjang adalah: {panjang}</p>
    <p>Nilai juta10 adalah: {juta10}</p>
    <p>Nilai y adalah: {nilai_y}</p>
    """
if __name__ == '__main__':
    app.run(debug=True)