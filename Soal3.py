banyak = int(input("Masukkan banyaknya angka yang ingin dimasukkan: "))

total = 0
i = 1
while i <= banyak:
    angka = float(input("Masukkan angka : "))
    total += angka
    i += 1

rata_rata = total / banyak
print("Rata-rata dari angka yang dimasukkan adalah :", rata_rata)



