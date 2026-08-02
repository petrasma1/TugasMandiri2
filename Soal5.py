N = int(input("Masukkan angka ke-N: "))

a, b = 0, 1
count = 1
while count <= N:
    fib = a
    a, b = b, a + b
    count += 1

print("Bilangan Fibonaccinya adalah :", fib)
