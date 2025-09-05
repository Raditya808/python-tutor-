# latiham konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam Celcius: "))

print(f"suhu adalah ", celcius, "Celcius")

print("================================================")
# reamur
# rumus nya yaitu R = C * 4/5
reamur = (4/5) * celcius

print(f"reamur ke celcius adalah", reamur)

print("================================================")
# fahremheit
# rumus nya yaitu f = 9/5 * c + 32
fahrenheit = (9/5) * celcius + 32
print(f"fahrenheit ke celcius adalah", fahrenheit)

print("================================================")
# kelvin
# rumus kelvin adalah K = C + 273

kelvin = celcius + 273
print(f"kelvin ke celcius adalah", kelvin)
print("================================================")


