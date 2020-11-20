#2009106001 = 1 + 10 = 11
angka = int(input("Masukkan nim anda + 10 : "))
x = 1
y = 1
while (y <= angka):
    print(x)
    x += 1
    if (x == 10):
        x -= 9
    y += 1
