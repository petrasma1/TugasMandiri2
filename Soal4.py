N = int(input("Masukkan angka ke-N: "))

faktorial = 1
i = 1
while i <= N:
    faktorial *= i
    i += 1

print("Faktorialnya adalah :", faktorial)
