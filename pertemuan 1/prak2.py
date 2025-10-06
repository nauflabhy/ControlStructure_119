a = float(input("Masukan angka pertama: "))
b = float(input("Masukan angka kedua: "))
c = float(input("Masukan angka ketiga: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
elif c >= a and c >= b:
    largest = c
else:
    print("Tidak ada nilai terbesar")

print("Angka terbesar adalah:", largest)