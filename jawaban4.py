def hollow_triangle(n):
    if n == 1:
        print("***")
        return False

    atas = [" " * (n - 1) + "***" + " " * (n - 1)]
    bawah = ["**" * ((n)) + '*']
    mid = []
    for i in range(n-2, 0, -1):
        mid.append((" " * i) + "**" + (" " * ((2 * n) - (2 * i) - 3)) + "**" + (" " * i))
    
    print(atas[0])

    for i in mid:
        print(i)

    print(bawah[0])
    
baris = int(input('Masukkan Jumlah Baris : '))
hollow_triangle(baris)